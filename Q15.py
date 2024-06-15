#!/usr/bin/env python3
import csv

print("Enter name of file: ")
name = input()
file = open(name, "r")
csv_reader = csv.reader(file)
for line in csv_reader:
    print(line)
