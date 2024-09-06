#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if (i > j or i == j):
            continue
        else:
            print("{}{}".format(i, j), end=", ")
