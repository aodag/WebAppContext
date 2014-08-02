# -*- coding:utf-8 -*-

import contextlib
from sqlalchemy.orm import (
    sessionmaker,
)


@contextlib.contextmanager
def session_scope(sessionmaker):
    session = sessionmaker()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
