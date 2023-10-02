
def main(num):
  total = 0
  for i in range(num):
    if i % 3 == 0 or i % 5 == 0:
      total += i
  return total 
  
if __name__ == "__main__":
  assert main(10) == 23
  print(main(1000))
