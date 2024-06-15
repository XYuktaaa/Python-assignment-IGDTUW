#!/usr/bin/env python3
print("Enter text: ")
text = input()
file = open("text.txt", "a")
file.write(text)
