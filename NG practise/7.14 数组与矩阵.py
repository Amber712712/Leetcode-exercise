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

 
4 

        
    
    
  
  
    
