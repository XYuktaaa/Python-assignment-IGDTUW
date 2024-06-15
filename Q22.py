#!/usr/bin/env python3
print("Enter numbers: ")
a = input()
b = a.split(' ')
num = []
for n in b:
    num.append(int(n))
max = num[0]
min = num[0]
for n in num:
    if n > max:
        max = n
    if n < min:
        min = n
print(f'max is {max}')
print(f'min is {min}')
print(num)
