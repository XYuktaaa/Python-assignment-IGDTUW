#!/usr/bin/env python3
print("Enter string: ")
a = input()
words = a.split(' ')
b = ''
for word in words:
    word = word.capitalize()
    b += word + ' '

print(b)
