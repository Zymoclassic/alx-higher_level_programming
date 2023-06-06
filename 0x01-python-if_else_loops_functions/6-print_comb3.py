#!/usr/bin/python3
# prints combination of numbers

for digitone in range(0, 10):
    for digittwo in range(digitone + 1, 10):
        if digitone == 8 and digittwo == 9:
            print("{}{}".format(digitone, digittwo))
        else:
            print("{}{}".format(digitone, digittwo), end=", ")
