def not_string(word):
  if word.startswith("not",0,3):
    return word
  else:
    return "not"+ " " + word
