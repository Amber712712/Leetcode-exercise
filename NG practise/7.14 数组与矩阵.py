1 把数组中的 0 移到末尾 左指针左边都是非0
def func(nums):
  l,r=0,0
  while r<len(nums):
    if nums[r]!=0:
      nums[r],nums[l]=nums[l],nums[r]
      l+=1
    r+=1
  return nums
2 改变矩阵维度
def func(nums,r,c):
  m=len(nums)
  n=len(nums[0])
  if m*n!=r*c:
    return nums
  new=[[0]*c for i in range(r)]
  for x in range(m*n):
    new[x//c][x%c]=nums[x//n][x%n]
  return new

3 有序矩阵的 Kth Element
 二分法
（1）利用helper 确定num>=k
 (2)利用二分法将使得left right 相同返回left
1 3 4
4 5 6
7 8 9

def func(matrix,k):
  n=len(matrix)
  def helper(mid):
    i=n-1
    j=0
    num=0
    while i >=0 and j<n:
      if matrix[i][j]<=mid:
        num+=i+1
        j+=1
      else:
        i-=1
    return num>=k 
  递增矩阵大于等于一个数的个数
  
  left,right=matrix[0][0],matrix[n-1][n-1]
  mid=(left+right)//2
  while left<right:
    if helper(mid):
      right=mid
    else:
      left=mid+1
  return left
  利用二分法最终使得left right 两边相等
  
利用heap:
  将每列元素最开头的元素入heap
  如果这一行元素没弹完，则将这一列下一个元素入heap
  
def func(matrix,k):
  heap=[(matrix[i][0],i,0) for i in range(len(matrix))]
  heapq.heapify(heap)
  for i in range(k-1):
    val,x,y=heapq.heappop(heap)
    while y<len(matrix[0]):
      heapq.heappush(heap,(matrix[x][y+1],x,y+1))
  return heapq.heappop(heap)

 
4 数组相邻差值的个数
将数组分为两组 n=9 k=5   1 9 2 8 3 4 5...
第一组：1，n,2,n-1...
第二组：递增或递减
def func(n,k):
  ans=[]
  l=1
  r=n
  for i in range(k):
    if i%2==0:
      ans[i]=l
      l+=1
    else:
      ans[i]=r
      r-=1
  
  for i in range(k,n):
    if k%2==0:
      ans[i]=r
      r-=1
  return ans

5 数组的度
def func(nums):
  dic={}
  for i,num in enumerate(nums):
    if num in dic:
      dic[num][0]+=1
      dic[num][2]=i
    else:
      dic[num]=(1,i,i)
      
  maxcount,res=0,0
  for c,left,right in dic:
    if c>maxcount:
      maxcount=c
      res=right-left+1
    elif c==maxcount:
      if (s:=right-left+1)<res:
        res=s
        
  return res

6 对角元素相等的矩阵
def func(matrix):
  for i in range(1,len(matrix)):
    for j in range(1,len(matrix[0])):
      if matrix[i][j]!=matrix[i-1][j-1]:
        return False
  return True

7 嵌套数组
1 有向图内环节点
def func(nums):
  vis=[False]*len(nums)
  n=len(nums)
  ans=0
  for i in range(n):
    cnt=0
    while not vis[i]:
      vis[i]=True
      i=nums[i]
      cnt+=1
    ans=max(ans,cnt)
    
    
    
  
      
       
      
    
                            
  
        
      
      
  
  
  
  
      
  
  
  

        
    
    
  
  
    
