# setup.py is python-3.7.4 source file

import os
import shutil
import setuptools

from stopwatch import Version


setuptools.setup(
    name = 'stopwatch', 
    version = '{MAJOR}.{MINOR}.{REVISION}'.format(
        MAJOR = Version.major, 
        MINOR = Version.minor, 
        REVISION = Version.revision
    ), 
    url = 'https://smallso.gitbook.io/stopwatch/python/overview', 
    license = 'Apache License 2.0', 
    author = 'SmallSO Labs.', 
    author_email = 'support@xiaoyy.org', 
    description = 'Programs for Python run high-precision stopwatch.', 
    packages = [
        'stopwatch'
    ],
    python_requires = '>=3.6', 
    zip_safe = False
)

wheel_file_name: str = './dist/stopwatch-{VERSION_NUMBER}-py3-none-any.whl'.format(
    VERSION_NUMBER = '{MAJOR}.{MINOR}.{REVISION}'.format(
        MAJOR = Version.major, 
        MINOR = Version.minor, 
        REVISION = Version.revision
    )
)

if os.access(wheel_file_name, os.R_OK):
   shutil.copy(wheel_file_name, './dist/stopwatch-release-py3-none-any.whl')
