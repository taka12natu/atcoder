n,x = map(int, input().split())
ab = [list(map(int,input().split())) for _ in range(n)]
dp = [[0]*(x+1) for _ in range(n)]
for i in range(n):
  dp[i][0]=1
for i in range(n):
  for j in range(x):
    if dp[i][j]==1 and j+ab[i][0]<=x:
      dp[i+1][j+ab[i][0]]==1
    if dp[i][j]==1 and j+ab[i][1]<=x:
      dp[i+1][j+ab[i][1]]==1
print(dp)