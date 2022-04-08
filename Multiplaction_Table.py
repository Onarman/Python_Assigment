i =int(input("enter a positive integer number less than 10please : "))

while i <= 10 :
  j = 1
  while j <= 10:
    print('{0}  *  {1}  =  {2}'.format(i, j, i*j))
    j += 1
  print("===========")
  i += 1