# setup.py is python-3.7.4 source file

import os
import shutil
import setuptools

from stopwatch import Version


# define get_readme_text function

def get_readme_text():
    readme_file_context = None

    try:
        readme_file_context = open('./README.md', mode = 'r', encoding = 'utf-8')
        return readme_file_context.read()
    finally:
        if readme_file_context:
            readme_file_context.close()


setuptools.setup(
    name = 'stopwatch', 
    version = '{MAJOR}.{MINOR}.{REVISION}'.format(
        MAJOR = Version.major, 
        MINOR = Version.minor, 
        REVISION = Version.revision
    ), 
    url = 'https://smallso.gitbook.io/stopwatch/python/overview', 
    license = 'Apache License 2.0', 
    author = 'MIT License', 
    author_email = 'support@xiaoyy.org', 
    description = 'Programs for Python run high-precision stopwatch.', 
    long_description = get_readme_text(), 
    long_description_content_type = 'text/markdown', 
    packages = [
        'stopwatch'
    ],
    python_requires = '>=3.6', 
    zip_safe = False, 
    classifiers = (
        'Programming Language :: Python :: 3', 
        'License :: OSI Approved :: MIT License', 
        'Operating System :: OS Independent', 
        'Development Status :: 5 - Production/Stable'
    )
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
