
1 长度最小的数组
利用前缀和+二分法 二分法查找右边界：符合条件的最右边的数字 
延申：递增数组中，找到差值小于等于某值的最右边的数字
def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if not nums:
            return 0
        pre=[0]
        for i in range(len(nums)):
            pre.append(pre[-1]+nums[i])
        
        l,r=0,len(pre)
        res=float('inf')
        mid=-1
        for i in range(len(pre)):
            d=pre[i]-target
            if d<0:
                continue
            l=0
            r=i
            while l<=r:
                mid=(l+r)//2
                if pre[mid]<=d:
                    ans=mid
                    l=mid+1
                else:
                    r=mid-1
            res=min(res,i-ans)
        if mid==-1:
            return 0
        else:
            return res
          
2 除了自己之外的乘积 创造2列表 分别为左乘积 右乘积
def func(nums):
        n=len(nums)
        l,r=[0]*n,[0]*n
        l[0]=1
        r[n-1]=1
        
        for i in range(1,n):
                l[i]=l[i-1]*nums[i-1]
        for i in range(n-2,-1,-1):
                r[i]=r[r+1]*nums[i+1]
        
3 实现矩阵前缀和
 def __init__(self, matrix: List[List[int]]):
        m,n=len(matrix),len(matrix[0]) if matrix else 0
        self.sum=[[0]*(n+1) for i in range(m)]
        s=self.sum
        for i in range(m):
            for j in range(1,n+1):
                s[i][j]=s[i][j-1]+matrix[i][j-1]
        



    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        s=self.sum
        return sum(s[i][col2+1]-s[i][col1] for i in range(row1,row2+1))

4 "*"代表盘子 "|"代表蜡烛 
左边：找出右边的蜡烛
右边：找出左边的蜡烛
def func(s):
  if not s:
    return 0
  n=len(s)
  pre=[0]*n
  sum_=0
  left=[0]*n
  l=-1
  for i,chr in enumerate(s):
    if chr=='*':
      sum_+=1
    else:
      l=i
    pre[i]=sum
    left[i]=l
    
  right,r=[0]*n,-1
  for i in range(n-1,-1,-1):
    if s[i]=="|":
      r=i
    right[i]=r
    
  ans = [0] * len(queries)
  for i, (x, y) in enumerate(queries):
    x, y = right[x], left[y]
    if x >= 0 and y >= 0 and x < y:
      ans[i] = preSum[y] - preSum[x]
      return ans
    

5 
    
    

 
    
  



    

  

                        


        

        
        

