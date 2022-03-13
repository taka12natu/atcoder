s = input()
i = 0
while i < len(s)+1:
  if s[i:i+6] == "eraser": 
    i = i+6
  elif s[i:i+5] == "erase":
    i = i+5
  elif s[i:i+5] == "dream":
    if s[i+5:i+11] == "eraser":
      i = i+11
    elif s[i+5:i+10] == "erase":
      i = i+10
    elif s[i:i+7] == "dreamer":
      i = i+7
    else:
      i = i+5
  else:
    print("NO")
    exit()
  if i==len(s):
    print("YES")
    exit()
  