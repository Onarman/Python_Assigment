n = int(input("enter a number pleaase : "))
sum = 0

while (n > 0):
  last_num = n % 10
  sum +=last_num
  n  //= 10

print(f"sum of digits of given number = {sum}")