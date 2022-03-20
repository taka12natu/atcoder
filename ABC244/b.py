n = int(input())
t = list(input())
x,y = 0,0
d = "r"
for i in t:
  if i == "S":
    if d == "r": 
      x += 1
    elif d == "l":
      x -= 1
    elif d == "t": 
      y += 1
    elif d == "b": 
      y -= 1
  elif i == "R":
    if d == "r": 
      d = "b"
    elif d == "l":
      d = "t"
    elif d == "t": 
      d = "r"
    elif d == "b": 
      d = "l"
print(x,y)
