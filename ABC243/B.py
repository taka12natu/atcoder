n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
cnt = 0
for i in range(n):
  if a[i] == b[i]:
    cnt += 1
print(cnt)
cnt_2 = 0
for num in a:
  if num in b:
    cnt_2 += 1
print(cnt_2-cnt)