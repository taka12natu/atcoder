n,x = map(int, input().split())
S = input()
arr = []
for s in S:
  if s == 'U' and len(arr)>0 and arr[-1] != 'U':
    arr.pop()
  else:
    arr.append(s)
for a in arr:
  if a=='R':
    x = x*2+1
  elif a=='L':
    x = x*2
  elif a=='U':
    x = x//2
print(x)
