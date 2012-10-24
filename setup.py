from distutils.core import setup

from sekhon import __version__

setup(name='sekhon',
        version=__version__,
        author="Christopher Small",
        author_email="csmall@fhcrc.org",
        scripts=['sekhon.py'],
        py_modules=['sekhon'],
        requires=['scipy'])

