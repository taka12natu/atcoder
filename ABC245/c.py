n,k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a_jud = [False]*n
b_jud = [False]*n
a_jud[0]=b_jud[0]=True
for i in range(1,n):
  if a_jud[i-1]:
    if abs(a[i-1] - a[i]) <= k:
      a_jud[i] = True
    if abs(a[i-1] - b[i]) <= k:
      b_jud[i] = True
  if b_jud[i-1]:
    if abs(b[i-1] - a[i]) <= k:
      a_jud[i] = True
    if abs(b[i-1] - b[i]) <= k:
      b_jud[i] = True
if a_jud[n-1] or b_jud[n-1]:
  print('Yes')
else:
  print("No")