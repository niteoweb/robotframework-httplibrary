#!/usr/bin/env python

import sys
from distutils.core import setup

CLASSIFIERS = """
Programming Language :: Python
Programming Language :: Python :: 2.7
Programming Language :: Python :: 3.5
Topic :: Software Development :: Testing
"""[1:-1]

from os.path import join, dirname
long_description = open(join(dirname(__file__), 'README.rst',)).read()

PY3 = sys.version_info[0] == 3

install_requires = [
    'webtest>=2.0',
    'jsonpatch',
    'jsonpointer',
    'future',
]

if PY3:
    install_requires.append('robotframework-python3')
else:
    install_requires.append('robotframework')

setup(
    name='robotframework-httplibrary',
    version="0.4.2-beta.1",
    description='Robot Framework keywords for HTTP requests',
    long_description=long_description,
    author='Filip Noetzel',
    author_email='filip+rfhttplibrary@j03.de',
    url='https://github.com/peritus/robotframework-httplibrary',
    license='Beerware',
    keywords='robotframework testing testautomation web http webtest',
    platforms='any',
    zip_safe=False,
    classifiers=CLASSIFIERS.splitlines(),
    package_dir={'': 'src'},
    install_requires=install_requires,
    packages=['HttpLibrary']
)
