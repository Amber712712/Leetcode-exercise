1 有序matrix的Kth elements
def func(matrix,k):
  
  def helper(mid):
    m=len(matrix)
    n=0
    num=0
    while m>=0 and n<len(matrix):
      if matrix[m][n]<=mid:
        num+=m
        n+=1
      else:
        m-=1
    return num>=k
  
  left=matrix[0][0]
  right=matrix[n-1][n-1]
  while left<right:
    if helper(mid):
      right=mid
    else:
      left=mid+1
  return left

2 用heap 选出kth element
def func(matrix):
  hp=[(matrix[i][0],i,0) for i in range(len(matrix)))]
  heapq.heapify(hp)
  for i in range(k-1):
    val,x,y =heapq.heappop(hp)
    if y!=n-1:
      heapq.heappush(hp,(matrix[x][y+1],x,y+1))
      
  return heapq.heappop(hp)[0]

3 
def func(lists):
  hp=[]
  heapq.heapify(hp)
  for l in lists:
    head=l
    if head:
      heapq.heappush(hp,(head.val,head))
  dummy=ListNode(0)
  cur=dummy
  while hp:
    _,node=heapq.heappop(hp)
    cur.next=node
    cur=cur.next
    if node.next:
      heapq.heappush((node.next.val,node.next))
      
  return dummy.next

4 嵌套数组
def func(nums):
  vis=[False]*len(nums)
  ans=0
  for i in range(len(nums)):
    cnt=0
    while not vis[i]:
      vis[i]=True
      i=nums[i]
      cnt+=1
    ans=max(ans,cnt)
  return ans


5 
    
  
  
  
 
  

  
  
