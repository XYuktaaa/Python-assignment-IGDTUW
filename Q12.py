#!/usr/bin/env python3
print("Enter number: ")
a = int(input())
sum = 0
while a > 0:
    sum += a % 10
    a = int (a / 10)
print(sum)
