# solution-1
from math import factorial as fac

print(fac(5))


# solution-2
n =int(input("enter a number : "))
result = 1
for i in range(1,n+1):
  result*=i
  
print(result)


# solution-3
n =int(input("enter a number : "))
result = 1
i = 1

while (i <= n):
  result*=i
  i += 1
print(result)
