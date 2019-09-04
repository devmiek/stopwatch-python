# stopwatch.errors.py is python-3.7.4 source file

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


# define StopwatchNameError exception class

class StopwatchNameError(Error):
    '''
    The Stopwatch unique name is invalid.

    This exception is thrown, for example, when trying to get a Stopwatch 
        instance that does not exist from Stopwatch Manager or add a 
        Stopwatch instance with the same name.
    '''

    pass


# define MaxLimitError exception class

class MaxLimitError(Error):
    '''
    The indicator exceeded the maximum limit.

    For example, adding a Stopwatch instance to the Stopwatch manager 
        will raise this exception when the maximum number of instances 
        limit is exceeded.
    '''

    pass
