""" 
衝突が発生するケース
・yが等しい場合 
・xが小さい方がR かつ xが大きい方がL
Rのi<Lのi  が条件

y座標が同じ時、
rかつmin_rより小さかったら更新
lかつmax_lより大きかったら更新

y座標違ったら、
min_r<max_lならprintしてexit、
上以外ならmax_lとmin_rを0にして再度
"""

n = int(input())
row = [list(map(int, input().split())) for i in range(n)]
s = list(input())
for i in range(n):
  row[i].append(s[i])
row.sort(key=lambda x:x[1])
min_r = 10**9
max_l = 0
r, l = 0, 0
""" for i in range(n):
  if row[i][1] == row[i+1][1]:
    if row[i][2]=="R" and row[i][0] < min_r: 
      min_r = row[i][0] 
    if row[i][2]=="L" and row[i][0] > max_l: max_l = row[i][0]
  else:
    if min_r < max_l: 
      print("Yes")
      exit()
    else:
      min_r = 10**9
      max_l = 0
  if i+2 == n:
    print("No")
    exit() """

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
    if cnt > n-1: exit() 
  if min(r) < max(l): 
    print("Yes")
    exit()
print('No')
    

