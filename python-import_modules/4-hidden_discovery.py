#!/usr/bin/python3
if (__name__ == "__main__"):
    import hidden_4
    per_line = dir(hidden_4)
    per_line = sorted(per_line)
    for i in per_line:
        if (i[0:2] == "__"):
            continue
        print(i)
