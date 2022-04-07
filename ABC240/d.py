n = int(input())
a = list(map(int,input().split()))
tube = []
cnt = []
tube.append(a[0])
cnt.append(1)
print(1)
for i in range(1,n):
  tube.append(a[i])
  if len(tube) >= 2 and tube[-1] == tube[-2]:
    cnt.append(cnt[-1]+1)
    if cnt[-1] == tube[-1]:
      del tube[-tube[-1]:]
      del cnt[-cnt[-1]:]
  else:
    cnt.append(1)
  print(len(cnt))
 
