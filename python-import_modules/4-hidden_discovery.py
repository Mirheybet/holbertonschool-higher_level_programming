#!/usr/bin/python3
import hidden_4
def sortlines(perline):
    per_lines = dir(perline)
    per_lines = sorted(per_lines)
    for i in per_lines:
        if (i[0:2] == "__"):
            continue
        print("{}".format(i))
if __name__ == "__main__":
    sortlines(hidden_4)
