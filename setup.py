try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description':       'Converts communication files to tex',
    'author':            'Bastian Loehrer',
    'url':               'tba',
    'download_url':      'tba',
    'author_email':      'bastianloehrer@gmail.com',
    'version':           '0.1',
    'install_requires': ['nose'],
    'packages':         ['com2tex'],
    'scripts':          [],
    'name':              'com2tex'
}

setup(**config)
