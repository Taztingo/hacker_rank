#!/bin/python3

import sys


n = int(input().strip())
for i in range(n):
  output = ""
  stairs = i + 1
  spaces = n - stairs
  output += " " * spaces
  output += "#" * stairs
  print(output)