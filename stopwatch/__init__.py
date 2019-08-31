# stopwatch.__init__.py is python-3.7.4 source file

# Copyright 2019 SmallSO Labs.
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

'''
The package Stopwatch implements statistics on runtime.

By using Stopwatch, you can quickly record and manage 
    your program's high-precision runtime.
'''

from stopwatch.version import Version

from stopwatch.errors import StatusError
from stopwatch.errors import LapNameError

from stopwatch.watch import Stopwatch
from stopwatch.watch import StopwatchStatus


# define __all__ variable

__all__: list = [
    Version, 
    StatusError, 
    LapNameError, 
    Stopwatch, 
    StopwatchStatus
]


# define __version__ variable

__version__: str = '{MAJOR}.{MINOR}.{REVISION}'.format(
    MAJOR = Version.major, 
    MINOR = Version.minor, 
    REVISION = Version.revision
)
