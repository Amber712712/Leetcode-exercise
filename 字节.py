1 最长子序列： 最长公共子串
用二维数组代表字串公共长度
def func(t1,t2):
  m,n=len(t1),len(t2)
  dp=[[0]*(n+1) for i in range(m+1)]
  
  for i in range(1,m+1):
    for j in range(1,n+1):
      if t1[i-1]==t2[j-1]:
        dp[i][j]=dp[i-1][j-1]+1
      else:
        dp[i][j]=max(dp[i-1][j],dp[i][j-1])
  return dp[m][n]


