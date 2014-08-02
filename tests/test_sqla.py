# -*- coding: utf-8 -*-

from unittest import mock

def test_session_scope_commit():
    from webappcontext.sqla import session_scope
    mock_maker = mock.Mock()

    with session_scope(mock_maker):
        pass

    mock_maker.return_value.commit.assert_called_with()


def test_session_scope_rollback():
    from webappcontext.sqla import session_scope
    mock_maker = mock.Mock()

    try:
        with session_scope(mock_maker):
            raise ValueError("dummy")
    except ValueError as e:
        assert e.args == ("dummy",)

    mock_maker.return_value.rollback.assert_called_with()
