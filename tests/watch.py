# tests.watch.py is python-3.7.4 source file

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
This module implements unit testing of the block watch.py 
    for stopwatch to ensure it works correctly.
'''

import time

from errors import TestError

from stopwatch import Stopwatch
from stopwatch import StopwatchStatus


# define tests function

def tests():
    test_stopwatch: Stopwatch = Stopwatch()

    test_stopwatch = Stopwatch(
        default_precision = 3
    )

    test_stopwatch.start()

    if not isinstance(test_stopwatch.lap('tests::test1'), float):
        raise TestError('lap() return value is unexpected')

    if not isinstance(test_stopwatch.lap('tests::test2'), float):
        raise TestError('lap() return value is unexpected')

    if not isinstance(test_stopwatch.lap(), float):
        raise TestError('lap() return value is unexpected')

    time.sleep(1)

    total_of_watch: float = test_stopwatch.get_watch()

    if not isinstance(total_of_watch, float):
        raise TestError('get_watch() return value is unexpected')

    if total_of_watch < 0.9 or total_of_watch > 1.5:
        raise TestError('get_watch() return value is error')
    
    is_has: bool = test_stopwatch.has_lap('tests::test1')

    if not isinstance(is_has, bool):
        raise TestError('has_lap() return value is unexpected')
    
    if not is_has:
        raise TestError('has_lap() return value is error')

    if test_stopwatch.get_lap_count() != 3:
        raise TestError('get_lap_count() return value is unexpected')
    
    if test_stopwatch.get_status() != StopwatchStatus.Started:
        raise TestError('get_status() return value is unexpected')
    
    if not isinstance(test_stopwatch.stop(), float):
        raise TestError('stop() return value is unexpected')
    
    if not isinstance(test_stopwatch.get_lap(
        lap_name = 'tests::test1',
        lap_precision = 3
    ), float):
        raise TestError('get_lap() return value is unexpected')

    if not isinstance(test_stopwatch.get_lap(
        lap_name = 'tests::test2'
    ), float):
        raise TestError('get_lap() return value is unexpected')

    if not isinstance(test_stopwatch.get_lap_by_number(3), float):
        raise TestError('get_lap_by_number() return value is unexpected')

    if not isinstance(test_stopwatch.get_average_of_laps(), float):
        raise TestError('get_average_of_laps() return value is unexpected')
    
    if not isinstance(test_stopwatch.get_laps(), list):
        raise TestError('get_laps() return value is unexpected')
    
    test_stopwatch.reset()

    if test_stopwatch.has_lap('tests::test1'):
        raise TestError('reset() error')
