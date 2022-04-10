n = int(input("enter a positive number : "))
count = 0
while n > 0:
  n = n // 10
  count += 1

print("\n Number of digits in a given number = %d" %count)