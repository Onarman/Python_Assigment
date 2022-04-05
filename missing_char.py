def missing_char(word, n):
  while n < len(word) :
    return word[:n] + word[n+1:]
