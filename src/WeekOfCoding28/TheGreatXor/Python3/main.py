def find_closest_value(number):
  power = 0
  while(2**power < number):
    power += 1
  return 2**power

def main():
  lines = int(input())
  countList = []
  for line in range(lines):
    query = int(input()) 
    closest = find_closest_value(query)
    value = closest - 1
    if(closest != query):
      value -= query
    countList.append(str(value))
  print("\n".join(countList))

main()