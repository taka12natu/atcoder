n,x = map(int, input().split())
ab = [list(map(int,input().split())) for _ in range(n)]
dp = [[0]*(x+1) for _ in range(n+1)]
dp[0][0]=1
for i in range(n):
  a = ab[i][0]
  b = ab[i][1]
  for j in range(x):
    if dp[i][j]==1 and j+a<=x:
      dp[i+1][j+a]=1
    if dp[i][j]==1 and j+b<=x:
      dp[i+1][j+b]=1
if dp[n][x]==1:
  print('Yes')
else:
  print('No')