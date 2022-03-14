""" 
・tが奇数の時、x+yは奇数でなければならず、その逆も然り
・t < x+y は成立しない
2回目以降の移動の際には条件がどう変わるか
・t-(pre-t)< x+y-(pre(x+y))
※１つ前の時点との差で考える
※偶数、奇数の条件は不変

n = int(input())
flg = False
pret = 0
prexy = 0
for i in range(n):
  t,x,y = list(map(int, input().split()))
  if t%2 == (x+y)%2 and t-pret >= x+y-prexy:
    pret = t
    prexy = x+y
    flg = True
  else:
    flg = False
    break
if flg:
  print('Yes')
else:
  print('No')


→テストケース after_contest_01.txt だけクリアできず
 """

n = int(input())
flg = False
pret = 0
prex = 0
prey = 0
for i in range(n):
  t,x,y = list(map(int, input().split()))
  d = abs(x-prex)+abs(y-prey)
  if ((t-pret)-d)%2 == 0 and t-pret >= d:
    pret = t
    prex = x
    prey = y
    flg = True
  else:
    flg = False
    break
if flg:
  print('Yes')
else:
  print('No')
