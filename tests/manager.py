# tests.manager.py is python-3.7.4 source file

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
This module implements unit testing of the block manager.py 
    for stopwatch to ensure it works correctly.
'''

from errors import TestError

from stopwatch import Stopwatch
from stopwatch import StopwatchManager


# define tests function

def tests():
    test_manager: StopwatchManager = StopwatchManager()

    test_manager = StopwatchManager(
        max_stopwatch_count = 100
    )

    if not isinstance(test_manager.create('tests::test1'), Stopwatch):
        raise TestError('create() return value is unexpected')

    test_manager.remove('tests::test1')
    
    if not isinstance(test_manager.create_and_start('tests::test1'), Stopwatch):
        raise TestError('create_and_start() return value is unexpected')
    
    test_manager.remove('tests::test1')
    test_manager.add('tests::test1', Stopwatch())

    test_manager.get('tests::test1').start()
    test_manager.get('tests::test1').stop()

    if not isinstance(test_manager.has('tests::test1'), bool):
        raise TestError('has() return value is unexpected')
    
    if not test_manager.has('tests::test1'):
        raise TestError('has() error')

    test_manager.remove('tests::test1')

    for count in range(100):
        test_manager.create('tests::test' + str(count))

    if test_manager.get_count() != 100:
        raise TestError('get_count() return value is unexpected')
    
    test_manager.starts()
    test_manager.get_watchs()
    test_manager.stops()
    test_manager.resets()
    
    test_manager.clear()
