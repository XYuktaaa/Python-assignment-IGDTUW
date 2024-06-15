#!/usr/bin/env python3
print("Enter name of file: ")
name = input()
file = open(name, "r")
text = file.read()
print(text)
