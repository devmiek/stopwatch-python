# stopwatch.watch.py is python-3.7.4 source file

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
The current module definition package Stopwatch's Stopwatch class implementation.
'''

import time

from stopwatch.errors import StatusError
from stopwatch.errors import LapNameError


# define MAX_STOPWATCH_PRECISION const

MAX_STOPWATCH_PRECISION: int = 8    # Maximum Stopwatch precision.


# define StopwatchStatus enum

class StopwatchStatus:
    '''
    An enumerator that indicates the status of the Stopwatch.

    Members:
        Stopped, int: Stopwatch has stopped or never started.
        Started, int: The stopwatch has started.
    '''

    Stopped: int = 0
    Started: int = 1


# define Stopwatch class

class Stopwatch:
    '''
    A stopwatch for runtime.

    By using Stopwatch, you can quickly and easily 
    count the running time of each process.
    '''

    # define __init__ function

    def __init__(self,
        default_precision: int = 3
    ):
        '''
        Constructs an instance of the Stopwatch class object.

        Args:
            default_precision, int: The default precision (number of decimal places) 
                of the stopwatch, whose value should be less than or equal to the 
                constant MAX_STOPWATCH_PRECISION.
        
        Raises:
            ValueError: The data type or value of the parameter is invalid.
        '''

        if not default_precision or not isinstance(default_precision, int):
            raise ValueError('<default_precision> value invalid')
        
        if default_precision > MAX_STOPWATCH_PRECISION:
            raise ValueError('<default_precision> value should be less than ' + str(MAX_STOPWATCH_PRECISION))

        self.__stopwatch_precision: int = default_precision
        self.__stopwatch_laps: dict = dict()

        self.__stopwatch_start_count: float = None
        self.__stopwatch_last_count: float = None
        self.__stopwatch_total_count: float = float()

        self.__stopwatch_status: int = StopwatchStatus.Stopped


    # define get_status function

    def get_status(self) -> int:
        '''
        Get the status of the Stopwatch.

        Returns:
            Returns the current state of Stopwatch whose value is indicated using 
                the StopwatchStatus enumerator.
        '''

        return self.__stopwatch_status


    # define start function

    def start(self):
        '''
        Start running Stopwatch.

        Raises:
            StatusError: Stopwatch has started.
        '''

        if self.__stopwatch_status != StopwatchStatus.Stopped:
            raise StatusError('stopwatch has started')

        self.__stopwatch_start_count = float(time.perf_counter())
        self.__stopwatch_status = StopwatchStatus.Started


    # define stop function

    def stop(self) -> float:
        '''
        Stop running Stopwatch.

        Returns:
            Returns the total time (in seconds) that Stopwatch will count 
                from the first time to the stop time.

        Raises:
            StatusError: Stopwatch has stopped or never started.
        '''

        stopwatch_stop_count: float = float(time.perf_counter())

        if self.__stopwatch_status != StopwatchStatus.Started:
            raise StatusError('stopwatch has stopped')

        self.__stopwatch_total_count += (stopwatch_stop_count - self.__stopwatch_start_count)
        self.__stopwatch_status = StopwatchStatus.Stopped

        return self.get_watch(None)


    # define lap function

    def lap(self,
        lap_name: str = None
    ) -> float:
        '''
        Record the time once.

        Record the interval from the last record to the current time.
            If this is the first record, record the interval from the 
            beginning to the current.
        
        Args:
            lap_name, str: Record name.
        
        Returns:
            The time (in seconds) to return this record.
        
        Raises:
            ValueError: The data type or value of the parameter is invalid.
            StatusError: Stopwatch has not started.
            LapNameError: The same record name already exists.
        '''

        stopwatch_lap_count: float = float(time.perf_counter())

        if lap_name:
            if not isinstance(lap_name, str):
                raise ValueError('<lap_name> value invalid')
            
            if lap_name in self.__stopwatch_laps:
                raise LapNameError('lap name already exists: ' + lap_name)

        if self.__stopwatch_status != StopwatchStatus.Started:
            raise StatusError('stopwatch did not start')

        if not self.__stopwatch_last_count:
            self.__stopwatch_last_count = self.__stopwatch_start_count
        
        self.__stopwatch_laps[lap_name if lap_name else 'lap_' + str(len(
            self.__stopwatch_laps) + 1)] = stopwatch_lap_count - self.__stopwatch_last_count
        
        self.__stopwatch_last_count = stopwatch_lap_count
        return stopwatch_lap_count


    # define reset function

    def reset(self):
        '''
        Reset Stopwatch.

        Statistics such as Laps and total duration are cleared after reset.

        Raises:
            StatusError: Stopwatch has not stopped.
        '''

        if self.__stopwatch_status != StopwatchStatus.Stopped:
            raise StatusError('stopwatch has started')
        
        self.__stopwatch_laps.clear()
        self.__stopwatch_start_count = None
        self.__stopwatch_last_count = None
        self.__stopwatch_total_count = float()


    # define has_lap function

    def has_lap(self,
        lap_name: str
    ) -> bool:
        '''
        Check if the specified timing record exists.

        Args:
            lap_name, str: Record the name. If it is an anonymous record, 
                the name is lap_ + number(for example: lap_1).
        
        Returns:
            Returns True if it exists, or False if it does not exist.
        
        Raises:
            ValueError: The data type or value of the parameter is invalid.
        '''

        if not lap_name or not isinstance(lap_name, str):
            raise ValueError('<lap_name> value invalid')
        
        return lap_name in self.__stopwatch_laps


    # define get_lap function

    def get_lap(self,
        lap_name: str,
        lap_precision: int = None
    ) -> float:
        '''
        Get the statistical time (in seconds) by record name.

        Args:
            lap_name, str: Record the name. If it is an anonymous record, 
                the name is lap_ + number(for example: lap_1).
            lap_precision, int: Record precision (number of decimal places).
                If not provided or not, the default precision value of the 
                stopwatch will be used.  whose value should be less than or 
                equal to the constant MAX_STOPWATCH_PRECISION.

        Returns:
            Returns the recording time (in seconds) with a data type of float.

        Raises:
            ValueError: The data type or value of the parameter is invalid.
            LapNameError: There is no such record.
        '''

        if not lap_name or not isinstance(lap_name, str):
            raise ValueError('<lap_name> value invalid')
        
        if not lap_precision:
            lap_precision = self.__stopwatch_precision
        elif not isinstance(lap_precision, int):
            raise ValueError('<lap_precision> value invalid')
        elif lap_precision > MAX_STOPWATCH_PRECISION:
            raise ValueError('<lap_precision> value should be less than ' + str(MAX_STOPWATCH_PRECISION))

        try:
            return round(self.__stopwatch_laps[lap_name], lap_precision)
        except KeyError:
            raise LapNameError('no such lap: ' + lap_name)


    # define get_lap_by_number function

    def get_lap_by_number(self,
        lap_number: int,
        lap_precision: int = None
    ) -> float:
        '''
        Get the statistical time (in seconds) by record number.

        Args:
            lap_number, int: Record number, starting with 1.
            lap_precision, int: Record precision (number of decimal places).
                If not provided or not, the default precision value of the 
                stopwatch will be used.  whose value should be less than or 
                equal to the constant MAX_STOPWATCH_PRECISION.

        Returns:
            Returns the recording time (in seconds) with a data type of float.

        Raises:
            ValueError: The data type or value of the parameter is invalid.
            LapNameError: There is no such record.
        '''

        return self.get_lap('lap_' + str(lap_number), lap_precision)


    # define get_average_of_laps function

    def get_average_of_laps(self,
        average_precision: int = None
    ) -> float:
        '''
        Get the average (in seconds) of all timing records.

        Args:
            average_precision, int: average precision (number of decimal places).
                If not provided or not, the default precision value of the 
                stopwatch will be used.  whose value should be less than or 
                equal to the constant MAX_STOPWATCH_PRECISION.
        
        Returns:
            Returns the average (in seconds) of all timing records.
        
        Raises:
            ValueError: The data type or value of the parameter is invalid.

        '''

        if not average_precision:
            average_precision = self.__stopwatch_precision
        if not isinstance(average_precision, int):
            raise ValueError('<average_precision> value invalid')
        if average_precision > MAX_STOPWATCH_PRECISION:
            raise ValueError('<average_precision> value should be less than: ' + str(MAX_STOPWATCH_PRECISION))

        if len(self.__stopwatch_laps) == 0:
            return 0

        total_of_laps: float = 0

        for lap_name in self.__stopwatch_laps:
            total_of_laps += self.__stopwatch_laps[lap_name]
        
        return round(total_of_laps / len(self.__stopwatch_laps), average_precision)


    # define get_laps function

    def get_laps(self) -> list:
        '''
        Get all timing record names.

        Returns:
            Returns a list of all the timed record names.
        '''

        return list(self.__stopwatch_laps.keys())


    # define get_lap_count function

    def get_lap_count(self) -> int:
        '''
        Get the number of timed records.

        Returns:
            The number of timed records.
        '''

        return len(self.__stopwatch_laps)


    # define get_watch function

    def get_watch(self,
        watch_precision: int = None
    ) -> float:
        '''
        Gets the statistical time (in seconds) that Stopwatch is from start to finish.

        Args:
            watch_precision, int: Watch precision (number of decimal places).
                If not provided or not, the default precision value of the 
                stopwatch will be used.  whose value should be less than or 
                equal to the constant MAX_STOPWATCH_PRECISION.
        
        Returns:
            Returns the statistical time (in seconds) that Stopwatch is from start to finish.
        
        Raises:
            StatusError: Stopwatch has not stopped.
            ValueError: The data type or value of the parameter is invalid.
        '''

        if not watch_precision:
            watch_precision = self.__stopwatch_precision
        elif not isinstance(watch_precision, int):
            raise ValueError('<watch_precision> value invalid')
        elif watch_precision > MAX_STOPWATCH_PRECISION:
            raise ValueError('<watch_precision> value should be less than ' + str(MAX_STOPWATCH_PRECISION))
        
        if self.__stopwatch_status == StopwatchStatus.Started:
            return round(self.__stopwatch_total_count + 
                ((float(time.perf_counter()) - self.__stopwatch_start_count)), watch_precision)
        elif self.__stopwatch_status == StopwatchStatus.Stopped:
            return round(self.__stopwatch_total_count, watch_precision)
        else:
            raise StatusError('stopwatch status is invalid')
