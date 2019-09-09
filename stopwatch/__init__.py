# stopwatch.__init__.py is python-3.7.4 source file

# Copyright (c) 2019 SmallSO Labs.
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

'''
The package Stopwatch implements statistics on runtime.

By using Stopwatch, you can quickly record and manage 
    your program's high-precision runtime.

Developer documentation: https://smallso.gitbook.io/stopwatch/v/en/python/overview
'''

from stopwatch.version import Version

from stopwatch.errors import StatusError
from stopwatch.errors import LapNameError
from stopwatch.errors import StopwatchNameError

from stopwatch.watch import Stopwatch
from stopwatch.watch import StopwatchStatus

from stopwatch.manager import StopwatchManager


# define __all__ variable

__all__: list = [
    'Version',

    'StatusError',
    'LapNameError',
    'StopwatchNameError',

    'Stopwatch',
    'StopwatchStatus',
    
    'StopwatchManager',
]


# define __version__ variable

__version__: str = '{MAJOR}.{MINOR}.{REVISION}'.format(
    MAJOR = Version.MAJOR,
    MINOR = Version.MINOR,
    REVISION = Version.REVISION
)


# define default_manager variable

default_manager: StopwatchManager = StopwatchManager()
