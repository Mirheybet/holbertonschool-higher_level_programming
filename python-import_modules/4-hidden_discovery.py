#!/usr/bin/python3
if (__name__ == "__main__"):
    import hidden_4
    per_lines = dir(hidden_4)
    per_lines = sorted(per_lines)
    for i in per_lines:
        if (i[0:2] == "__"):
            continue
        print("{}".format(i))
