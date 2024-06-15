#!/usr/bin/env python3
print("Enter two words:")
a = input()
b = input()

if sorted(a) == sorted(b):
    print("They are anagrams")
else:
    print("They are not anagrams")
