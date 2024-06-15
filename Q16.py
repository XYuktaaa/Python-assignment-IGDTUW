#!/usr/bin/env python3
from collections import Counter
print("Enter string: ")
a = input()
c = Counter(a)
print(c.most_common())
