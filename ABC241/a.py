a = list(map(int, input().split()))
k = a[0]
for _ in range(2):
  k = a[k]
print(k)
