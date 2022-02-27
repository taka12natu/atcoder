n = int(input())
arr = list(map(int,input().split()))
cnt = 0
flg = True
while True:
  for i, value in enumerate(arr):
    if value % 2 == 0:
       arr[i] = int(value / 2)
    else:
      flg = False
      break
  if flg == False:
    break
  else:
    cnt += 1
print(cnt)