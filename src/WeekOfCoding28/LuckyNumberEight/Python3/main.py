import math

def count_divisible_combinations(number):
  divisible = 0
  combinations = []

  for char in number:
    newCombinations = [char]

    if is_divisible(int(char)):
      divisible += 1
    for combination in combinations:
      newCombination = combination + char
      newCombinations.append(newCombination)
      if is_divisible(int(newCombination)):
        divisible += 1

    combinations.extend(newCombinations)

  return divisible


def is_divisible(combination):
  return combination % 8 == 0


def calculate_lucky(divisible):
  return divisible % (10**9 + 7)


def main():
  input()
  number = str(input())
  divisible = count_divisible_combinations(number)
  print(str(calculate_lucky(divisible)))

main()