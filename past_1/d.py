""" 
１からNまで正しく入った配列compareと問題の配列aをソートしたものを順に比較
重複した値yの場合、「比較した値が異なる」かつ「a[i]==a[i-1]」である
書き換えられ存在しない値xの場合、「比較した値が異なる」かつ「compare[i+1]==a[i]」
→xはset関数で調べられる
"""

n = int(input())
a = [int(input()) for i in range(n)]
compare = [i for i in range(1,n+1)]
x = list(set(compare) - set(a))
if not x:
  print('Correct')
  exit()
else:
  a.sort()
  for i,num in enumerate(a):
    if a[i] == a[i+1]:
      y = a[i]
      break
  print(y,x[0])
""" 
  TLEになってしまう。dupの部分が遅いのかも

n = int(input())
a = [int(input()) for i in range(n)]
compare = [i for i in range(1,n+1)]
dup = [x for x in set(a) if a.count(x) > 1]
if len(dup) == 0:
  print('Correct')
else:
  y = dup[0]
  x = list(set(compare) - set(a))[0]
  print(y,x)

"""