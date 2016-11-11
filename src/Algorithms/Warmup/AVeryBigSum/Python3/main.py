#!/bin/python3

import sys


n = int(input().strip())
val = 0
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
for value in arr:
    val += value
print(val)