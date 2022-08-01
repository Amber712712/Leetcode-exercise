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
def func(s):
  if not s:
    return 0
  n=len(s)
  lookup=set()
  start,end=0,0
  min_len=n+1
  
  while end<n:
   
    while s[end] in lookup:
      lookup.remove(s[start])
      start+=1
    min_len=min(min_len,end-start+1)
    lookup.add(s[end])
    
 
6 假设你有两个数组，一个长一个短，短的元素均不相同。找到长数组中包含短数组所有的元素的最短子数组，其出现顺序无关紧要。
def func(big,small):
  if len(big)<len(small):
    return []
  need=len(small)
  left,right=0,0
  n=len(big)
  resleft=0
  dic=collections.Counter(small)
  
  while right<n:
    if big[right] in dic:
      if dic[big[right]]>0:
        need-=1
      dic[big[right]]-=1
      
    while need==0:
      if left>resleft:
        resleft=left
        
      if big[left] in dic:
        if dic[big[left]]>=0:
          need+=1
        dic[big[left]]+=1
      left+=1
    end+=1
  return resleft

7 
pre=[0]*n
sum_=0
for i in range(n):
  if s[i]=="*":
    sum_+=1
  else:
    pre[i]=sum_

右边：
right=-1
r=[0]*n
for i in range(n-1,-1,-1):
  if s[i]=="|":
    right=i
  r[i]=right
  
  
8 
def func(s):
  
  while i<=j:
    if s[i] not in s:
      i+=1
    if s[j] not in s:
      j-=1
    else:
      
      



  
  
  
  

  
    
      
      
      
  
  
 
  
  
  
  
    
  
  
  
 
  

  
  
