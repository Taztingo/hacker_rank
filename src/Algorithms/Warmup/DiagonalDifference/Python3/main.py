#!/bin/python3

import sys


n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)

left = 0
right = 0
for row in range(n):
    left += a[row][row]
    right += a[row][ n - row - 1]
    
difference = abs(left-right)
print(difference)