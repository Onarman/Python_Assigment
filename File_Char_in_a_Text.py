def count_char(text, char):
  count = 0
  for i in text:
    if i == char:
      count += 1
  return count

with open("istiklal_marsı.txt","r") as f:
  text = f.read()
print(count_char(text,"O"))