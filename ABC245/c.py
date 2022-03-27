n,k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
cnt = 0
arr = []
for i in range(n-1):
  if abs(a[i] - a[i+1]) <= k or abs(a[i] - b[i+1]) <= k :
    arr.append(a[i])
  elif abs(b[i] - b[i+1]) <= k or abs(b[i] - a[i+1]) <= k:
    arr.append(b[i])
if len(arr) != n-1:
  print("No")
else:
  for i in range(len(arr)-1):
    if abs(arr[i]-arr[i+1]) > k:
      print("No")
      exit()
  print('Yes')
  