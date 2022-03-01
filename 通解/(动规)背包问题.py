0-1背包
1 分为等子集
##注意边界值 dp[...][0]=true  dp[0][...]=false 放或不放

def func(nums): 
  s=sum(nums)
  m=max(nums)
  n=len(nums)
  
  if s%2!=0:
    return False
  if m>s/2:
    return False
  if n<2:
    return False
  t=s/2
  dp=[[False]*(t+1) for i in range(n+1)]
  for i in range(n+1):
    dp[i][0]=True
  for i in range(1,n+1):
    for j in range(1,t+1):
      if nums[i-1]>j:
        dp[i][j]=dp[i-1][j]
      else:
        dp[i][j]=dp[i-1][j] or dp[i-1][j-nums[i-1]]
        
2 背包问题； 体积固定 值最大 T为体积  ###放或不放
def func(nums,val,t):
  n=len(nums)
  dp=[[0]*(t+1) for i in range(n+1)]
  
  for i in range(1,n+1):
    for j in range(1,t+1):
      if j<nums[i-1]:
        dp[i][j]=dp[i-1][j]
      else:
        dp[i][j]=max(dp[i-1][j],dp[i-1][j-nums[i-1]]+val[i-1])
        
 return dp[-1][-1]
完全背包问题  可用硬币的类型有无限个
3 零钱兑换  写一个函数来计算可以凑成总金额的硬币组合数
def func(nums,t):
  n=len(nums)
  dp=[[0]*(t+1) for i in range(n+1)]
  for i in range(n+1):
    dp[i][0]=1
  for i in range(1,n+1):
    for j in range(1,t+1):
      if j<nums[i-1]:
        dp[i][j]=dp[i-1][j]
      else:
        dp[i][j]=dp[i-1][j]+dp[i-1][j-nums[i-1]]
        
  return dp[-1][-1]




      
      
