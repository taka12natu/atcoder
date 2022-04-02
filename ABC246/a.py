x1,y1 = map(int,input().split())
x2,y2 = map(int,input().split())
x3,y3 = map(int,input().split())
x = [x1,x2,x3]
if x[0] == x[1]:
  xa = x[2]
elif x[1] == x[2]:
  xa = x[0]
else:
  xa = x[1]
y = [y1,y2,y3]
if y[0] == y[1]:
  ya = y[2]
elif y[1] == y[2]:
  ya = y[0]
else:
  ya = y[1]
print(xa,ya)
