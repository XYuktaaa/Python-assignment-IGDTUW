#!/usr/bin/env python3
import string
print("Enter string: ")
a = input()
b = ''
for c in a:
    if c not in '.,!@#$%<<+`:;+>\\|&/)}({-})`?':
        b += c
print(b)
