"""
Simple script to display sensor values on terminal.

Use something like this to run it (requires wide terminal):

  pyboard.py /dev/ttyACM0 read-sensors.py
"""

import microbit

def print_array(prefix, array, end="\n"):
    fmt = "{:>7}|" * len(array)
    print(prefix, fmt.format(*array), end=end)


while True:

    min_array = None
    max_array = None

    print("       acc_x|  acc_y|  acc_z|")

    # 100 samples per batch
    for _ in range(100):

        # collect sensor values into array
        array = []
        array.extend(microbit.accelerometer.get_values())

        # update min_array, max_array
        if min_array is None:
            min_array, max_array = array, array
        else:
            min_array = [min(v) for v in zip(min_array, array)]
            max_array = [max(v) for v in zip(max_array, array)]

        # print current and wait
        print_array("    ", array, end="\r")
        microbit.sleep(50)

    # print min/max values for last batch
    print_array("min:", min_array)
    print_array("max:", max_array)
    print()
