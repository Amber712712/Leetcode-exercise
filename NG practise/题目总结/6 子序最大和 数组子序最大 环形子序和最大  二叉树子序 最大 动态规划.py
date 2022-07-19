1 数组的最大子序和
def func(nums):
  if not nums:
     return 0
  dp=[0 for i in range(len(nums)]
  dp[0]=nums[0]
  for i in range(1,len(nums)):
      if nums[i]>0:
         dp[i]=dp[i-1]+nums[i]
      else:
         dp[i]=nums[i]
  return max(dp)
  
2 二叉树的最大路径和


3 环形子序和最大 注意全为负数的时候 返回max(max_dp)
在中间/在两边
。。。最大。。。
。。。最小。。。
                       
                       
      
                       
                       
                       
                       
                       
                       
                       
                       
                       
                       
                       
                       
    

