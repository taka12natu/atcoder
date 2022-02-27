a = int(input())
b = int(input())
c = int(input())
n = int(input())
sum = 0
cnt = 0
for a_i in range(a+1):
  for b_i in range(b+1):
    for c_i in range(c+1):
      sum = 500*a_i + 100*b_i + 50*c_i
      if sum == n:
        cnt += 1
print(cnt)