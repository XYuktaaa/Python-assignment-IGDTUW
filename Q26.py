#!/usr/bin/env python3
print("Enter string: ")
a = input()
print("Enter 0 for prefix otherwise for suffix:")
mode = int(input())
if mode:
    print("Enter suffix: ")
else:
    print("Enter prefix: ")

string = input()

boo = False
if mode:
    boo = a.endswith(string)
else:
    boo = a.startswith(string)

does = '' if boo else 'doesnt'
modetext = 'suffix' if mode else 'prefix'
print(f'Given string {does} start with {modetext}')
