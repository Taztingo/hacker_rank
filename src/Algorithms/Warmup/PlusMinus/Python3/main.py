#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
positive = 0
negative = 0
zero = 0
for element in arr:
  if(element < 0):
    negative += 1
  elif(element == 0):
    zero += 1
  else:
    positive += 1

print(positive / n)
print(negative / n)
print(zero / n)