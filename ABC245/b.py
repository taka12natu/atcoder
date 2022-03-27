n = int(input())
s = list(map(int, input().split()))
if sum(s) == 0:
  print(1)
  exit()
arr = [0 for _ in range(2001)]
for i in s:
  arr[i] = 1
for i,x in enumerate(arr):
  if x == 0:
    print (i)
    exit()
