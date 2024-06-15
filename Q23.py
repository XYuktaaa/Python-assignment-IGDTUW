#!/usr/bin/env python3
print("Enter 1 for celcius to fahrenheit, 2 for vice versa: ")
mode = int(input())
print("Enter temperature value:")
temp = int(input())
if (mode == 1):
    print(f'Temperature in fahrenheit: {(temp * 9/5) + 32}')
else:
    print(f'Temperature in celcius: {(temp + 32) * 5/9}')
