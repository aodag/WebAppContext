# -*- coding:utf-8 -*-
from . import sqla


class WebAppContext(object):
    def __init__(self, dbsession):
        self.dbsession = dbsession

    def query(self, *args, **kwargs):
        return self.dbsession.query(*args, **kwargs)


class WebAppContextMiddleware(object):
    def __init__(self, app, config):
        self.app = app
        self.config = config
        sqla.setup(self.config)

    def __call__(self, environ, start_response):
        sessionmaker = self.config['webappcontext.sqla.sessionmaker']
        with sqla.session_scope(sessionmaker) as dbsession:
            context = WebAppContext(
                dbsession=dbsession)
            environ['webappcontext.context'] = context
            return self.app(environ, start_response)
