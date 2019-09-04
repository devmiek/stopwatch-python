# syopwatch.manager.py is python-3.7.4 source file

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
The current module implements the Stopwatch class instance registration feature of stopwatch.
'''

from stopwatch.watch import Stopwatch
from stopwatch.watch import StopwatchStatus

from stopwatch.errors import StatusError
from stopwatch.errors import StopwatchNameError
from stopwatch.errors import MaxLimitError


# define StopwatchManager class

class StopwatchManager:
    '''
    Stopwatch multi-instance manager.

    By using StopwatchManager, you can easily manage 
        a batch of Stopwatch instances.
    '''
    
    # define __init__ function

    def __init__(self,
        max_stopwatch_count: int = None
    ):
        '''
        Constructs an instance of the StopwatchManager class object.

        Args:
            max_stopwatch_count, int: The maximum number of Stopwatch instances that 
                can be accommodated. If this parameter is not supplied or the value 
                is None, the number of instances is not limited.
            
        Raises:
            ValueError: The data type or value of the parameter is invalid.
        '''

        if max_stopwatch_count and not isinstance(max_stopwatch_count, int):
            raise ValueError('<max_stopwatch_count> value invalid')
        
        self.__max_stopwatch_count: int = max_stopwatch_count
        self.__stopwatch_instances: dict = dict()


    # define get function

    def get(self,
        stopwatch_name: str
    ) -> Stopwatch:
        '''
        Get a Stopwatch instance by name.

        Args:
            stopwatch_name, str: Stopwatch unique name.
        
        Returns:
            Returns the specified Stopwatch instance.
        
        Raises:
            ValueError: The data type or value of the parameter is invalid.
            StopwatchNameError: There is no such Stopwatch instance.
        '''

        if not stopwatch_name or not isinstance(stopwatch_name, str):
            raise ValueError('<stopwatch_name> value invalid')
        
        try:
            return self.__stopwatch_instances[stopwatch_name]
        except KeyError:
            raise StopwatchNameError('no such stopwatch: ' + stopwatch_name)

    
    # define add function

    def add(self,
        stopwatch_name: str,
        stopwatch_instance: Stopwatch
    ):
        '''
        Add a Stopwatch instance.

        Args:
            stopwatch_name, str: Stopwatch unique name.
            stopwatch_instance, Stopwatch: The Stopwatch instance object to be added.
        
        Raises:
            ValueError: The data type or value of the parameter is invalid.
            StopwatchNameError: There is already a Stopwatch instance with the same name.
            MaxLimitError: The number of Stopwatch instances has exceeded the limit of the 
                constructor method max_stopwatch_count parameter.
        '''

        if not stopwatch_name or not isinstance(stopwatch_name, str):
            raise ValueError('<stopwatch_name> value invalid')

        if not stopwatch_instance or not isinstance(stopwatch_instance, Stopwatch):
            raise ValueError('<stopwatch_instance> value invalid')
        
        if stopwatch_name in self.__stopwatch_instances:
            raise StopwatchNameError('stopwatch name already exists: ' + stopwatch_name)

        if self.__max_stopwatch_count:
            if len(self.__stopwatch_instances) >= self.__max_stopwatch_count:
                raise MaxLimitError('max stopwatch instance limit')

        self.__stopwatch_instances[stopwatch_name] = stopwatch_instance


    # define create function

    def create(self,
        stopwatch_name: str
    ) -> Stopwatch:
        '''
        Create and add a Stopwatch instance.

        Args:
            stopwatch_name, str: Stopwatch unique name.
        
        Returns:
            The Stopwatch instance created.
        
        Raises:
            ValueError: The data type or value of the parameter is invalid.
            StopwatchNameError: There is already a Stopwatch instance with the same name.
            MaxLimitError: The number of Stopwatch instances has exceeded the limit of the 
                constructor method max_stopwatch_count parameter.
        '''

        new_stopwatch: Stopwatch = Stopwatch()

        self.add(
            stopwatch_name = stopwatch_name,
            stopwatch_instance = new_stopwatch
        )

        return new_stopwatch

    
    # define create_and_start function

    def create_and_start(self,
        stopwatch_name: str
    ) -> Stopwatch:
        '''
        Create, add, and start a Stopwatch instance.

        Args:
            stopwatch_name, str: Stopwatch unique name.
        
        Returns:
            The Stopwatch instance created.
        
        Raises:
            ValueError: The data type or value of the parameter is invalid.
            StopwatchNameError: There is already a Stopwatch instance with the same name.
            MaxLimitError: The number of Stopwatch instances has exceeded the limit of the 
                constructor method max_stopwatch_count parameter.
        '''

        self.create(stopwatch_name).start()
        return self.get(stopwatch_name)


    # define remove function

    def remove(self,
        stopwatch_name: str
    ):
        '''
        Remove the Stopwatch instance with the specified name.

        Args:
            stopwatch_name, str: Stopwatch unique name.
        
        Raises:
            ValueError: The data type or value of the parameter is invalid.
            StopwatchNameError: There is already a Stopwatch instance with the same name.
        '''

        if not stopwatch_name or not isinstance(stopwatch_name, str):
            raise ValueError('<stopwatch_name> value invalid')
        
        try:
            del self.__stopwatch_instances[stopwatch_name]
        except KeyError:
            raise StopwatchNameError('no such stopwatch: ' + stopwatch_name)


    # define clear function

    def clear(self):
        '''
        Remove all Stopwatch instances.
        '''

        self.__stopwatch_instances.clear()


    # define has function

    def has(self,
        stopwatch_name: str
    ) -> bool:
        '''
        Check if the Stopwatch instance with the specified name exists.

        Args:
            stopwatch_name, str: Stopwatch unique name.
        
        Returns:
            There is a return of True; there is no return to False.
        
        Raises:
            ValueError: The data type or value of the parameter is invalid.
        '''

        if not stopwatch_name or not isinstance(stopwatch_name, str):
            raise ValueError('<stopwatch_name> value invalid')
        
        return stopwatch_name in self.__stopwatch_instances


    # define get_count function

    def get_count(self) -> int:
        '''
        Gets the number of Stopwatch instances that have been added.

        Returns:
            Returns the number of Stopwatch instances.
        '''

        return len(self.__stopwatch_instances)


    # define starts function

    def starts(self,
        stopwatch_names: list = None
    ) -> int:
        '''
        Start a specified batch or all of the Stopwatch instances.

        Note that the Stopwatch instance that has started will be skipped 
            instead of raising a StatusError exception.

        Args:
            stopwatch_names, list: A list of unique names for the Stopwatch instance 
                that needs to be started. If this parameter is not supplied or the 
                value is None, all Stopwatch instances are started.

        Returns:
            Returns the number of Stopwatch instances that actually started.
        
        Raises:
            ValueError: The data type or value of the parameter is invalid.
            StopwatchNameError: There is already a Stopwatch instance with the same name.
        '''

        if stopwatch_names and not isinstance(stopwatch_names, list):
            raise ValueError('<stopwatch_names> value invalid')

        real_start_count: int = 0

        try:
            for stopwatch_name in stopwatch_names if stopwatch_names else self.__stopwatch_instances:
                if self.__stopwatch_instances[stopwatch_name].get_status() == StopwatchStatus.Stopped:
                    self.__stopwatch_instances[stopwatch_name].start()
                    real_start_count += 1
        except KeyError:
            raise StopwatchNameError('no such stopwatch: ' + stopwatch_name)
        
        return real_start_count


    # define stops function

    def stops(self,
        stopwatch_names: list = None
    ) -> int:
        '''
        Stop the specified batch or all of the Stopwatch instances.

        Note that the stopped stopwatch instance will be skipped 
            instead of raising a StatusError exception.
        
        Args:
            stopwatch_names, list: A list of unique names for Stopwatch instances 
                that need to be stopped. If this parameter is not supplied or the 
                value is None, all Stopwatch instances are stopped.

        Returns:
            Returns the number of Stopwatch instances that were actually stopped.

        Raises:
            ValueError: The data type or value of the parameter is invalid.
            StopwatchNameError: There is already a Stopwatch instance with the same name.
        '''

        if stopwatch_names and not isinstance(stopwatch_names, list):
            raise ValueError('<stopwatch_names> value invalid')

        real_stop_count: int = 0

        try:
            for stopwatch_name in stopwatch_names if stopwatch_names else self.__stopwatch_instances:
                if self.__stopwatch_instances[stopwatch_name].get_status() == StopwatchStatus.Started:        
                    self.__stopwatch_instances[stopwatch_name].start()
                    real_stop_count += 1
        except KeyError:
            raise StopwatchNameError('no such stopwatch: ' + stopwatch_name)
        
        return real_stop_count


    # define resets function

    def resets(self,
        stopwatch_names: list = None
    ):
        '''
        Resets a specified batch or all Stopwatch instances.

        Args:
            stopwatch_names, list: A list of unique names for Stopwatch instances 
                that need to be reset. If this parameter is not supplied or the 
                value is None, all Stopwatch instances are reset.

        Raises:
            ValueError: The data type or value of the parameter is invalid.
            StopwatchNameError: There is already a Stopwatch instance with the same name.
        '''

        if stopwatch_names and not isinstance(stopwatch_names, list):
            raise ValueError('<stopwatch_names> value invalid')
        
        try:
            for stopwatch_name in stopwatch_names if stopwatch_names else self.__stopwatch_instances:
                if self.__stopwatch_instances[stopwatch_name].get_status() == StopwatchStatus.Started:
                    self.__stopwatch_instances[stopwatch_name].stop()

                self.__stopwatch_instances[stopwatch_name].reset()
        except KeyError:
            raise StopwatchNameError('no such stopwatch: ' + stopwatch_name)


    # define get_watchs function

    def get_watchs(self,
        stopwatch_names: list = None,
        watch_precision: int = None
    ) -> float:
        '''
        Gets the total duration (in seconds) of a specified 
            batch or all of the Stopwatch instances.
        
        Args:
            stopwatch_names, list: A list of unique names for the Stopwatch instance 
                that need to get the total duration. If this parameter is not supplied 
                or if the value is None, then all Stopwatch instances are obtained.
            watch_precision, int: Watch precision (number of decimal places).
                If not provided or not, the default precision value of the stopwatch 
                will be used.  whose value should be less than or equal to the constant 
                MAX_STOPWATCH_PRECISION.

        Returns:
            Returns the total time (in seconds) of the specified batch or all of the 
                Stopwatch instances.
        
        Raises:
            ValueError: The data type or value of the parameter is invalid.
            StopwatchNameError: There is already a Stopwatch instance with the same name.
            StatusError: Stopwatch has not stopped.
        '''

        if stopwatch_names and not isinstance(stopwatch_names, list):
            raise ValueError('<stopwatch_names> value invalid')

        watch_total: float = 0

        try:
            for stopwatch_name in stopwatch_names if stopwatch_names else self.__stopwatch_instances:
                watch_total += self.__stopwatch_instances[stopwatch_name].get_watch(watch_precision)
        except KeyError:
            raise StopwatchNameError('no such stopwatch: ' + stopwatch_name)
        except StatusError as error:
            raise StatusError('{ERROR_MESSAGE}: {STOPWATCH_NAME}'.format(
                ERROR_MESSAGE = str(error),
                STOPWATCH_NAME = stopwatch_name
            ))

        return watch_total
