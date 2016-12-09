#!/usr/bin/python
#NOT COMPLETED YET

def removeDuplicates(initialString):
  string = initialString
  for index in xrange(0, len(string)):
    if(initialString[index] not in characterCount):
      characterCount[initialString[index]] = 0
    else:
      characterCount[initialString[index]] += 1

    if(initialString[index] == initialString[index + 1]):
      string = string.replace(initialString[index], "")
  return string

def removeLeastKeyValue(dictionary):
  minimum = 999999999
  index = -1
  for(key in dictionary):
    minimum = min(minimum, dictionary[key])
  del dictionary[]

characterCount = {}
def twoCharacters(initialString, initialLength):
  string = initialString
  lastLength = -1
  while(len(string) != lastLength):
    characterCount = {}
    string = removeDuplicates(string)
    lastCharacterLength = -1
    while(lastCharacterLength != len(characterCount.keys())):
      character
    lastLength = len(string)





length = int(input().strip())
string = input().strip()
print(twoCharacters(string, length))