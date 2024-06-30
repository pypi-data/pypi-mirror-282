from __future__ import annotations

from typing import Any, Generator, Callable, Type, TypeVar

from sqlalchemy.orm import Session

from webapp_kit.persistence.database import DatabaseConnection


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


T = TypeVar("T", bound=SyncUnitOfWork)


def unit_of_work(cls: Type[T], connection: DatabaseConnection) -> Callable[[], Generator[T, None, None]]:
    def wrapped() -> Generator[SyncUnitOfWork, None, None]:
        with connection.connection() as session:
            with cls(session=session) as uow:
                yield uow

    return wrapped
