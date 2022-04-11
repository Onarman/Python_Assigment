# solution-1
a = int(input("enter a first number : "))
b = int(input("enter a second number : "))
i = 1

while i<=a and i<=b :
  if a % i == 0 and b % i == 0 :
    val = i
  i += 1

print(val)

#solution-2
from math import gcd

print(gcd(15,20))