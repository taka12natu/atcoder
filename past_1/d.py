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
  TLEになってしまう。dupの部分が遅いのかも
  """