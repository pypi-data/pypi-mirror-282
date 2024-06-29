from __future__ import annotations

from typing import Any, Generator, Callable, Type

from sqlalchemy.orm import Session

from src.persistence.database import DatabaseConnection


class SyncUnitOfWork:
    _session: Session

    def __init__(self, session: Session):
        self._session = session

    def __enter__(self) -> SyncUnitOfWork:
        return self

    def rollback(self) -> None:
        self._session.rollback()

    def commit(self) -> None:
        self._session.commit()

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        if exc_type is not None:
            self.rollback()
        else:
            self.commit()
        self._session.close()


def unit_of_work(cls: Type[SyncUnitOfWork], connection: DatabaseConnection) -> Callable[[], Generator[SyncUnitOfWork, None, None]]:
    def wrapped() -> Generator[SyncUnitOfWork, None, None]:
        with connection.connection() as session:
            with cls(session=session) as uow:
                yield uow
    return wrapped