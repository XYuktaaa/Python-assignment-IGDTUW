#!/usr/bin/env python3
print("Enter file to copy from:")
a = open(input(), 'r')
print("Enter file to paste to:")
b = open(input(), 'w')
b.write(a.read())
