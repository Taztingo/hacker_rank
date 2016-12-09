#!/usr/bin/python

def removePair(string):
  copy = string
  for index in range(0, len(string) - 1):
    if(string[index] == string[index + 1]):
      return copy[0:index] + copy[index+2:]
  return copy

def reduceString(string):
  reduced = string
  newReduced = removePair(reduced)
  while(reduced != newReduced):
    reduced = newReduced
    newReduced = removePair(reduced)

  if(reduced == ""):
    reduced = "Empty String"
  return reduced

print(reduceString(input()))