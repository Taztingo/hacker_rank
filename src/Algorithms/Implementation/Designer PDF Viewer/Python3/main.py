#!/bin/python3

import sys


def area(word, heights):
  width = len(word)
  height = 0
  for letter in word:
    index = ord(letter) - ord('a')
    if heights[index] > height:
      height = heights[index]
  return width * height


heights = [int(h_temp) for h_temp in input().strip().split(' ')]
word = input().strip()
print(str(area(word, heights)))