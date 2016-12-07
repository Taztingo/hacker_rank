#!/bin/python3

import sys

def hitHouse(houseLeft, houseRight, treeLocation, distance):
  location = treeLocation + distance
  return location >= houseLeft and location <= houseRight

def countHit(treeLocation, fruits):
  fruitHit = 0
  for fruit in fruits:
    if(hitHouse(houseLeft, houseRight, treeLocation, fruit)):
      fruitHit += 1
  return fruitHit

houseLeft, houseRight = input().strip().split(' ')
houseLeft, houseRight = [int(houseLeft), int(houseRight)]
appleTreeLocation, orangeTreeLocation = input().strip().split(' ')
appleTreeLocation, orangeTreeLocation = [int(appleTreeLocation), int(orangeTreeLocation)]
input()
apples = [int(apple_temp) for apple_temp in input().strip().split(' ')]
oranges = [int(orange_temp) for orange_temp in input().strip().split(' ')]

print(str(countHit(appleTreeLocation, apples)))
print(str(countHit(orangeTreeLocation, oranges)))