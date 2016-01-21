"""
Simple script to display sensor values on terminal.

Use something like this to run it (requires wide terminal):

  pyboard.py /dev/ttyACM0 read-sensors.py
"""

import microbit

def print_array(prefix, array, end="\n"):
    fmt = "{:>7}|" * len(array)
    print(prefix, fmt.format(*array), end=end)


# calibrate the compass
microbit.compass.calibrate()
print("Calibrating compass. Please spin the micro:bit", end="")

while microbit.compass.is_calibrating():
    microbit.sleep(400)
    print(".", end="")

print(" Calibrated!")


while True:

    min_array, max_array = None, None

    print("     "
          "  acc_x|"
          "  acc_y|"
          "  acc_z|"
          "  btn_a|"
          "  btn_b|"
          " comp_x|"
          " comp_y|"
          " comp_z|"
          " comp_h|"
         )

    # 100 samples per batch
    for _ in range(100):

        # collect sensor values into array
        array = []
        array.extend(microbit.accelerometer.get_values())

        array.append(microbit.button_a.is_pressed())
        array.append(microbit.button_b.is_pressed())

        array.append(microbit.compass.get_x())
        array.append(microbit.compass.get_y())
        array.append(microbit.compass.get_z())
        array.append(microbit.compass.heading())

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
