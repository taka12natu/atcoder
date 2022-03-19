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
解説参照
・各要素を０にした配列を用意し、数字に該当するインデックス（+1する）に個数をカウントしていく
個数が０の場合は書き換えられた数字x、個数が２の場合は重複している数字yと判定
n回の繰り返し処理で判定できる
"""
n = int(input())
a = [int(input()) for i in range(n)]
arr = [0 for x in range(n)]
for i,num in enumerate(a):
  arr[num-1] += 1
if arr.count(0):
  y = arr.index(2)+1
  x = arr.index(0)+1
  print(y, x)
else:
  print('Correct')
