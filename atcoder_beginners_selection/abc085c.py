""" n,price = map(int, input().split())
flg = False
for z in range(n+1):
  z_sum = z*1000
  for y in range(n+1):
    if z+y <= n:
      y_sum = y*5000
      for x in range(n+1):
        if x+y+z <= n:
          x_sum = x*10000
          if x_sum+y_sum+z_sum == price and x+y+z == n:
            flg = True
            break
          elif x_sum+y_sum+z_sum > price:
            break
    if flg or y_sum+z_sum > price:
      break
  if flg or z_sum > price:
    break

if flg == False:
  x,y,z = -1,-1,-1

print(x,y,z)
 """
n,price = map(int, input().split())
flg = False
for x in range(n+1):
  x_sum = x*10000
  for y in range(n+1):
    if x+y <= n:
      y_sum = y*5000
      z = n-x-y
      z_sum = z*1000
      if x_sum+y_sum+z_sum == price and x+y+z == n:
        flg = True
        break
      elif x_sum+y_sum+z_sum > price:
        break
  if flg:
    break

if flg == False:
  x,y,z = -1,-1,-1

print(x,y,z)
