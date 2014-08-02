from setuptools import setup


requires = [
    "Jinja2",
    "SQLAlchemy",
    "WebHelpers2>=2.0b5",
    "Babel",
]


setup(name="WebAppContext",
      install_requires=requires,
)
