#!/usr/bin/env python3
print("Enter a number: ")
x = int(input())
fac = x
for i in range(1, x):
    fac *= i
print("Factorial of number is: ")
print(fac)
