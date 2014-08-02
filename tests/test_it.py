import webtest
from webob.dec import wsgify
import sqlalchemy as sa
import sqlalchemy.orm as orm


metadata = sa.MetaData()
dummy_table = sa.Table(
    'dummy', metadata,
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("value", sa.Integer),
)

class DummyModel(object):
    def __init__(self, value=None):
        self.value = value

orm.Mapper(DummyModel, dummy_table)


@wsgify
def dummy_app(req):
    model = req.environ['webappcontext.context'].query(DummyModel).one()
    return "value = {0}".format(model.value)


def test_it():
    from webappcontext import WebAppContextMiddleware
    config = {
        "sqlalchemy.url": "sqlite:///",
        }

    app = WebAppContextMiddleware(
        dummy_app,
        config)
    engine = app.config['webappcontext.sqla.engine']
    metadata.create_all(engine)
    dbsession = app.config['webappcontext.sqla.sessionmaker']()
    dbsession.add(DummyModel(value=10))
    dbsession.commit()
    app = webtest.TestApp(app)
    res = app.get("/")

    assert res.text == "value = 10"


def test_greeting():
    """hello test """
    assert 1 + 1 == 2
