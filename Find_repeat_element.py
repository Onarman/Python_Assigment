"""
How do we test whether there are identical digits in a number sequence?
"""
liste=[1,2,3,4,5,4,4,6]
for i in liste:
  if liste.count(i)>=2:
    print('There are repeating elements',i)
    break
  else:
   pass