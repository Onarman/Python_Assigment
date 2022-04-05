def front_back(word):
  if len(word) > 1:
     b=word[-1]+word[1:-1]+word[0]
     return b
  else:
    return word[0]
