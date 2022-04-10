n = int(input("enter a positive number : "))
i = 0
first_n = 0
sec_n =1

while i < n:
  if i <= 1 :
    next =i
  else :
    next = first_n + sec_n
    first_n = sec_n
    sec_n = next
  print(next)
  i += 1