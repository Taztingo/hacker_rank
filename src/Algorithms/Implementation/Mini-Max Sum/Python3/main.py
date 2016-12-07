#!/bin/python

import sys


a,b,c,d,e = input().strip().split(' ')
array = [int(a),int(b),int(c),int(d),int(e)]
array.sort()
maxSum = 0
minSum = 0

for index in range(0, 4):
  minSum += array[index]

for index in range(1, 5):
  maxSum += array[-index]

print(str(minSum) + " " + str(maxSum))