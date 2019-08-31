# stopwatch.watch.py is python-3.7.4 source file

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
    ):
        '''
        Record the time once.

        Record the interval from the last record to the current time. 
            If this is the first record, record the interval from the 
            beginning to the current.
        
        Args:
            lap_name, str: Record name.
        
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
        
        self.__stopwatch_laps[lap_name if lap_name else 'lap' + str(len(
            self.__stopwatch_results) + 1)] = stopwatch_lap_count - self.__stopwatch_last_count
        
        self.__stopwatch_last_count = stopwatch_lap_count


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

        if self.__stopwatch_status != StopwatchStatus.Stopped:
            raise StatusError('stopwatch has started')

        if not watch_precision:
            watch_precision = self.__stopwatch_precision
        elif not isinstance(watch_precision, int):
            raise ValueError('<watch_precision> value invalid')
        elif watch_precision > MAX_STOPWATCH_PRECISION:
            raise ValueError('<watch_precision> value should be less than ' + str(MAX_STOPWATCH_PRECISION))
        
        return round(self.__stopwatch_total_count, watch_precision)
