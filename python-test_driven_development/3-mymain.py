#!/usr/bin/python3
say_my_name = __import__('3-my').say_my_name

say_my_name("John", "Smith")
say_my_name(3333, "White")
say_my_name(None)
say_my_name(ABC)
try:
    say_my_name(12, "White")
except Exception as e:
    print(e)
