# quickstart.py is python-3.7.4 source file

import time

from stopwatch import Stopwatch
from stopwatch import StopwatchStatus


# define main function

def main():

    # instantiate stopwatch

    demo_stopwatch: Stopwatch = Stopwatch(
        default_precision = 3   # ignorable
    )

    # make stopwatch start timing
    
    demo_stopwatch.start()

    # the first stage of the simulation program

    time.sleep(3)

    # it takes time to record the first phase of the program

    demo_stopwatch.lap('stage1')

    # the second stage of the simulation program

    time.sleep(1)

    # it takes time to record the second phase of the program

    demo_stopwatch.lap('stage2')
    
    # get the status of stopwatch

    if demo_stopwatch.get_status() == StopwatchStatus.Started:
        print('stopwatch is timing...')

    # stop and print the timing of the stopwatch
    
    print(
        (
            'total: {TOTAL_SECONDS} seconds\n'
            'stage1: {STAGE1_SECONDS} seconds\n'
            'stage2: {STAGE2_SECONDS} seconds'
        ).format(
            TOTAL_SECONDS = demo_stopwatch.stop(), 
            STAGE1_SECONDS = demo_stopwatch.get_lap('stage1'), 
            STAGE2_SECONDS = demo_stopwatch.get_lap('stage2')
        )
    )

    # reset stopwatch

    demo_stopwatch.reset()


# define virtual main function

if __name__ == '__main__':
    main()
