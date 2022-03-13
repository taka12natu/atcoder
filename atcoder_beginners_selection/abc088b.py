n = int(input())
arr = list(map(int,input().split()))
arr.sort(reverse=True)
a = 0
b = 0
for index, num in enumerate(arr):
  if index % 2 == 0:
    a = a + num
  else:
    b = b + num
print(a-b)