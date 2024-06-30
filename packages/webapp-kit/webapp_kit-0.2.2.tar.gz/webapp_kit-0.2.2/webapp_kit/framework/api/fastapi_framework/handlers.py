from abc import abstractmethod
from typing import Any

from fastapi import Depends

from webapp_kit.framework.api.fastapi_framework.jwt import token_from_header
from webapp_kit.persistence.asyncio import unit_of_work as async_uow
from webapp_kit.persistence.asyncio.unit_of_work import AsyncUnitOfWork
from webapp_kit.persistence.sync import unit_of_work as sync_uow
from webapp_kit.persistence.sync.unit_of_work import SyncUnitOfWork


class BaseHandler:
    pass


class BaseAuthenticationHandler(BaseHandler):
    token: str = Depends(token_from_header)


class AsyncAuthenticationHandler(BaseAuthenticationHandler):
    uow: AsyncUnitOfWork = Depends(async_uow.unit_of_work)

    @property
    @abstractmethod
    async def user(self) -> Any:
        raise NotImplementedError


class AuthenticationHandler(BaseAuthenticationHandler):
    uow: SyncUnitOfWork = Depends(sync_uow.unit_of_work)

    @property
    @abstractmethod
    def user(self) -> Any:
        raise NotImplementedError
