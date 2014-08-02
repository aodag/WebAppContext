# -*- coding:utf-8 -*-

import contextlib
from sqlalchemy import (
    engine_from_config,
)
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


def setup(config):
    engine = engine_from_config(config)
    config["webappcontext.sqla.engine"] = engine
    config["webappcontext.sqla.sessionmaker"] = sessionmaker(bind=engine)
