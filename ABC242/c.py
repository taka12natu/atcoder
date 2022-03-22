""" DP(動的計画法)問題 """
mod = 998244353
n = int(input())
dp = [[0]*10 for _ in range(n+1)]
for i in range(9):
  dp[0][i]= 1

for i in range(1,n):
  for j in range(9):
    if j == 0:
      dp[i][j] = (dp[i-1][j] + dp[i-1][j+1])%mod
    elif j == 8:
      dp[i][j] = (dp[i-1][j-1] + dp[i-1][j])%mod
    else:
      dp[i][j] = (dp[i-1][j-1] + dp[i-1][j] + dp[i-1][j+1])%mod
print(sum(dp[n-1])%mod)