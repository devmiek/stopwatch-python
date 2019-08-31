# quickstart.py is python-3.7.4 source file

import time

from stopwatch import Stopwatch
from stopwatch import StatusError


# define main function

def main() -> int:
    test_stopwatch: Stopwatch = Stopwatch(6)
    test_stopwatch.start()

    time.sleep(3)

    test_stopwatch.lap('test1')

    time.sleep(1)

    test_stopwatch.lap('test2')
    
    print('Total: ' + str(test_stopwatch.stop()))
    print('Test1: ' + str(test_stopwatch.get_lap('test1')))
    print('Test2: ' + str(test_stopwatch.get_lap('test2')))

    return 0


# define virtual main function

if __name__ == '__main__':
    main()
