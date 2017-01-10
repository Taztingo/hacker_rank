def meets_criteria(value, maximum):
  return (value ^ maximum) > maximum


def count_match_criteria(maximum, cache):
  counter = 0
  if maximum not in cache:
    for value in range(maximum - 1):
      if meets_criteria(value + 1, maximum):
        counter += 1
      cache[maximum] = counter
  else:
    counter = cache[maximum]
  return counter


def main():
  lines = int(input())
  cache = {}
  countList = []
  for line in range(lines):
    maximum = int(input())
    countList.append(str(count_match_criteria(maximum, cache)))
  print("\n".join(countList))

main()