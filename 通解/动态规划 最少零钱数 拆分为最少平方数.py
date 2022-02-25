1 零钱
def func(nums):
  dp=[0]+[float('inf')]*nums
  for i in range(1,nums):
    for j in coins:
      if i>=j:
        dp[i]=min(dp[i],dp[i-j]+1)
  if dp[-1]!=float('inf'):
    return dp[-1]
  else:
    return -1
2 平方数：
def func(nums):
  if not nums or nums==0:
    return 0
  dp=[0]+[float('int')]*nums
  
  for i in range(1,len(dp)):
    for j in range(1,int(sqrt(i))+1):
      dp[i]=min(dp[i],dp[i-j**2]+1)
      
    
    
