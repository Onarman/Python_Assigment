'''Given a string, return the count of the number of times that a substring length 2 appears in the string and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).'''

wrd = "xaxxaxaxx" 
def last2(str) :
  count = 0
  for i in range(len(str)-2) :
    print(str[i:i+2])
    if str[len(str)-2:] in str[i:i+2] :
      count += 1
  return count

last2(wrd)