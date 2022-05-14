#!/usr/bin/env python3

from importlib.resources import contents
import numbers
from operator import mod
from traceback import format_tb
import string

flag = []
with open("message.txt") as file_object:
    contents = file_object.read()
    # print(contents.split())
    # strings = contents.split()
    # for every_value in strings:
    #     print(every_value,type(every_value))
    #     int_value = int(every_value)
    #     print(int_value,type(int_value))
    numbers = [ int(val) for val in contents.split() ]
    for number in numbers:
        modulus = number % 37
        if modulus in range(26):
            flag.append(string.ascii_uppercase[modulus])
        elif modulus in range(26,36):
            flag.append(string.digits[modulus-26])
        else:
            flag.append("_")

# print(flag)
print("picoCTF{"+"".join(flag)+"}")
# print("picoCTF{%s}" " % " .join(flag))
