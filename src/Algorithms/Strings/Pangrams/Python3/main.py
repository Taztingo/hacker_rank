#!/usr/bin/python

def isPangram(string):
  dictionary = {}
  for key in string:
    if(key.isalpha()):
      dictionary[key.lower()] = True
  return len(dictionary.keys()) == 26

string = input()
if(isPangram(string)):
  print("pangram")
else:
  print("not pangram")