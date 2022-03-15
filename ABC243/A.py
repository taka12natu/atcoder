v,a,b,c = map(int, input().split())
arr = [a,b,c]
flg = False
i = 0
while flg == False:
  n = arr[i]
  v = v - n
  if v<0:
    if i == 0:
      print("F")
    elif i == 1:
      print("M")
    elif i == 2:
      print("T")
    flg = True
  i += 1
  if i > 2 and v>=0:
    i = 0