.. -*- coding:utf-8 -*-

========================
WebAppContext
========================

.. image:: https://travis-ci.org/aodag/WebAppContext.svg?branch=master
    :target: https://travis-ci.org/aodag/WebAppContext

USAGE
=======================



context object
======================

query
----------------------

``query`` method is querying ``SQLAlchemy`` session.

get_template
------------------------------

``get_template`` method is returning `Jinja2`` template object.

template
----------------------

shortcut for ``get_template(name).render(params)``.

