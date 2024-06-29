from datetime import datetime, timedelta
from typing import NewType

from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import jwt, JWTError

from src.framework.api.fastapi_framework.exceptions import UnauthorizedException, ExceptionDetail

AccessToken = NewType("AccessToken", str)
RefreshToken = NewType("RefreshToken", str)


class JWTTokens:
    def __init__(self, secret_key: str,
                 algorithm: str = "HS256"):
        self._secret_key = secret_key
        self._algorithm = algorithm

    def tokens(self, data: dict, access_token_expiration: timedelta, refresh_token_expiration: timedelta) -> tuple[
        AccessToken, RefreshToken]:
        access_token_payload = data.copy()
        refresh_token_payload = data.copy()

        access_token_expire = datetime.utcnow() + access_token_expiration
        refresh_token_expire = datetime.utcnow() + refresh_token_expiration

        access_token_payload.update({"exp": access_token_expire})
        refresh_token_payload.update({"exp": refresh_token_expire, "refresh": True})

        access_token = jwt.encode(
            access_token_payload, self._secret_key, algorithm=self._algorithm
        )

        refresh_token = jwt.encode(
            refresh_token_payload, self._secret_key, algorithm=self._algorithm
        )

        return AccessToken(access_token), RefreshToken(refresh_token)

    def decoded_access_token(self, token: str) -> dict:
        try:
            decoded_token = jwt.decode(
                token, self._secret_key, algorithms=[self._algorithm]
            )
            return decoded_token
        except JWTError:
            raise UnauthorizedException(detail=[ExceptionDetail(detail="Invalid token or expired token")])


def token_from_header(
    token: HTTPAuthorizationCredentials = Depends(HTTPBearer()),
) -> str:
    if token is None:
        raise UnauthorizedException(detail=[ExceptionDetail(detail="Missing authorization header")])
    return token.credentials
