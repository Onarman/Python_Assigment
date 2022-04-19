s =input("write a sentence : ")
v = input("choose a voice : ")

i = 0

while i < len(s):
  if(s[i] == v):
    print(f"{v} is found position {i+1}")
  i += 1