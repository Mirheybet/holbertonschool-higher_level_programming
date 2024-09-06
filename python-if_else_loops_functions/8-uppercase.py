#!/usr/bin/python3
def uppercase(str):
    str_cln = ""
    for ch in str:
        if (ord(ch) in range(97, 123)):
            str_cln += chr(ord(ch)-32)
        else:
            str_cln += ch
    print("{}".format(str_cln))
