number = int(input("enter a number : "))

basamak =str(number)

sum = 0

for i in basamak:
  i = int(i)
  sum += i**(len(basamak))

if number == sum:
  print(f"{number} is an Armstrong number")
else :
  print(f"{number} is NOT an Armstrong number")