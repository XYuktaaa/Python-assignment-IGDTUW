#!/usr/bin/env python3
print("Enter numbers: ")
a = input()
num = a.split(' ')
sum = 0
for n in num:
    sum += int(n)
print(f'sum is {sum}')
