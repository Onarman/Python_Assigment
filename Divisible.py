
"""Question: Write a program which will find all such 
numbers which are divisible by 7 but are not a multiple 
of 5, between 2000 and 3200 (both included). The numbers 
obtained should be printed in a comma-separated sequence 
on a single line."""

#HINT-1:range(#start,stop-1)
#HINT-2: "".join(iterable)

liste=[]

for numbers in range(2000,3201):
  if (numbers%7==0 )and (numbers%5!=0):
    liste.append(str(numbers))


print(",".join(liste))


#Output==>2002,2009,2016,2023,2037,2044,2051,2058,...3199