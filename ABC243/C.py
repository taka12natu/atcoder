""" 
衝突が発生するケース
・yが等しい場合 
・xが小さい方がR かつ xが大きい方がL
Rの最小値<Lの最大値  が条件
"""

n = int(input())
row = [list(map(int, input().split())) for i in range(n)]
s = list(input())
for i in range(n):
  row[i].append(s[i])
row.sort(key=lambda x:x[1])
cnt = 0
while cnt < n-1:
  r = []
  l = []
  y = row[cnt][1]
  while row[cnt][1] == y:
    if row[cnt][2] == "R":
      r.append(row[cnt][0])
    else:
      l.append(row[cnt][0])
    cnt += 1
    if cnt > n-1: break
  if r and l:
    if min(r) < max(l): 
      print("Yes")
      exit()
print('No')
    

