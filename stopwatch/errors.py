# stopwatch.errors.py is python-3.7.4 source file

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
The current module defines all exceptions for the package Stopwatch.
'''

# define Error exception class

class Error(Exception):
    '''
    A generic exception indicating the Stopwatch package.

    All exceptions defined in the current module are based on this exception. 
        Normally, you should not catch this exception.
    '''

    pass


# define StatusError exception class

class StatusError(Error):
    '''
    The Stopwatch status is invalid.

    For example, trying to start a Stopwatch that has already started or 
        trying to stop a Stopwatch that has stopped will cause this exception.
    '''

    pass


# define LapNameError exception class

class LapNameError(Error):
    '''
    The Stopwatch record name is invalid.

    For example, trying to get a record that does not exist or try 
        to add a record with the same name will cause this exception.
    '''

    pass
