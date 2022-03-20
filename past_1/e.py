n,q = map(int,input().split())
user = [["N" for i in range(n)] for i in range(n)]
for i in range(q):
  s = list(map(int,input().split()))
  if s[0] == 1:
    a = s[1]-1
    b = s[2]-1
    user[a][b] = "Y"
  elif s[0] == 2:
    a = s[1]-1
    for index,num in enumerate(user[a]):
      if user[index][a] == "Y":
        user[a][index] = "Y"
  elif s[0] == 3:
    a = s[1]-1
    a_follows = []
    for index,num in enumerate(user[a]): 
      if num == "Y":
        a_follows.append(index) #現時点でのaがフォローしているuserを書き出す※下のforをネストするとaがフォローしているユーザーが増えていく
    for a_follow in a_follows: 
      for index,num in enumerate(user[a_follow]): 
        if num == "Y" and index != a: # 自信をフォローしない
          user[a][index] = "Y"
for row in user:
  print(*row, sep="")

""" user = [list(map(int,input().split())) for i in range(n)] """
