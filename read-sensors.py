"""
Simple script to display sensor values on terminal.

Use something like this to run it (requires wide terminal):

  pyboard.py /dev/ttyACM0 read-sensors.py
"""

import microbit

def print_array(array, end="\n"):
    fmt = "{:>7}|" * len(array)
    print(fmt.format(*array), end=end)


while True:

    min_array = None
    max_array = None

    print("  acc_x|  acc_y|  acc_z|")

    # 100 samples per batch
    for _ in range(100):

        array = []

        array.extend(microbit.accelerometer.get_values())

        print_array(array, end="\r")

        if min_array is None:
            min_array = array
            max_array = array
        else:
            min_array = [min(x, y) for x, y in zip(min_array, array)]
            max_array = [max(x, y) for x, y in zip(max_array, array)]

        microbit.sleep(50)

    print_array(min_array)
    print_array(max_array)
    print()
