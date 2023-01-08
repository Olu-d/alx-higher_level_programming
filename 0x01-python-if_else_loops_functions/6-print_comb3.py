#!/usr/bin/python3
i = 0

while i <= 9:
    for j in range(i + 1, 10):
        if (i != 8):
            print("{}{}, ".format(i,j), end="")
        else:
            print("{}{}".format(i, j))
    i += 1

