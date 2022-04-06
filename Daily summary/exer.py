1 
def func(root1,root2):
  q=deque([root1])
  while q:
    n=q.pop(0)
    if n.val==root2.val:
      if func1(n,root2):
        return True
    if n.left:
      q.append()
      
    if n.right:
      q.append()
  return False
      
  直接用dfs
  
  对称树
  def func(r):
    if not r:
      return False
    q=deque([r])
    
    while q:
      for i in range(len(q)):
        n=q.popleft()
        
 def func(root):
  l=list()
  def dfs(root):
    l.append(root)
    dfs(root.left)
    dfs(root.right)
  
  for i in range(0,len(l)-1):
    l[i].left=None
    l[i].right=l[i+1]
    
    
  def func(root):
    stack,res=[],[]
    while root or stack:
      while root:
        stack.append(root)
        root=root.left
      tmp=stack.pop()
      res.append(tmp.val)
      root=tmp.right
      
  def func(root):
    
    def dfs(root,t):
      res=0
      if not root:
        return 0
      if root.val==t:
        res+=1
      return dfs(root.left,t-root.val)+dfs(root.right,t-root.val)
    if not root:
      return 0
    ret=0
    ret+=dfs(root.left)
    ret+=dfs(root.right)
    return ret
   
    
  q=[(root,root.val)]
  
  
 def func(root):
  self.ans=0
  def dfs(root):
    if not root:
      return 0
    left=dfs(root.left)
    right=dfs(root.right)
    if root.left:
      left=left+1 if root.left.val==root.val else 0
    if root.right:
      right=right+1 if root.right.val==root.val else 0
    self.ans=max(self.ans,left+right)
    return max(left,right)
  dfs(root)
  return ans

def func(root,t):
  def dfs(root,t):
    if not root:
      return 0
    res=0
    if root.val==t:
      res+=1
    res+=dfs(root.left,t-root.val)
    res+=dfs(root.right,t-root.val)
    return res
  if not root:
    return 0
  ret=dfs(root,t)
  ret+=dfs(root.left,t)
  
 def func(root1,root2):
  
  def bfs(a,b):
    
    q=[(a,b)]
    while q:
      a,b=q.pop(0)
      if not a and a.val!=b.val:
        return False
      if b.left:
        q.append((a.left,b.left))
      if b.right:
        q.append((a.right,b.right))
    return True
  
  q1=[root1]
  while q1:
    n=q1.pop(0)
    if n.val==root2.val:
      if bfs(n,root2):
        return True
    if n.left:
      q1.append(n.left)
    if n.right:
      q1.append(n.right)
  return False


def func(root):
  return max(dfs(root))
  
  
  def dfs(root):
    if not root:
      return [0,0]
    left=dfs(root.left)
    right=dfs(root.right)
    
    s=root.val+left[1]+right[1]
    nons=max(left)+max(right)
    
    return [s,nons]
  
    
def func(root,t):
def dfs(node,t,path,s):
  if not node:
    return 
  if not node.left and node.right and s==t:
    
    
def func(root):
  stack,res=[],[]
  while stack or root:
    while root:
      stack.append(root)
      root=root.left
    tmp=stack.pop()
    res.append(tmp.val)
    root=root.right
    
    
    
 def func(root):
  if not root:
    return False
  q=[root]
 s1=root.val
 s2=float('inf')
  while q:
    n=q.pop(0)
    if s1<n.val<s2:
      s2=n.val
    if n.left:
      q.append(n.left)
      q.append(n.right)
      
  
 def func(root):
  self.ans=float('inf')
  s1=root.val
  def dfs(node):
    if not root:
      return
    if s1<node.val<self.ans:
      self.ans=node.val
    dfs(root.left)
    dfs(root.right)
    
    dfs(root)
    return self.ans if self.ans!=float('inf') else -1
  
  
 def func(root,t):
  res=[]
  
  def dfs(root,path,t):
    nonlocal res
    if not root:
      return 
    if not root.left and not root.right and root.val==t:
      res.append(path+[root.val])
      
    dfs(root.left,path+[root.val],t-root.val)
    dfs()
    
  dfs(root,[],t)
  
  
  def func(a,b):
    if not a:
      return b
    if not b:
      return a
    new=TreeNode(a.val+b.val)
    new.left=func()
    new.right=func()
    return new
  
  
  def func(root):
    stack=[]
    while stack or root:
      while root:
        stack.append(root)
        root=root.left
      res=stack.pop()
      k-=1
      if k==0:
        return res
      
      
 def func(root):
  res=0
  def dfs(root):
    nonlocal res
    if not root:
      return 
    dfs(root.right)
    res+=root.val
    root.val=res
    dfs(root.left)
    
  dfs(root)
  return root


def func(root,p,q):
  if p.val<root.val and q.val<root.val:
    return func(root.left,p,q)
  
  
  def func(root,p,q):
    
    def dfs(root,p,q):
      if not root:
        return
      if root.val==p.val or root.val==q.val:
        return root.val
      left=dfs(root.left)
      right=dfs(root.right)
      if left and right:
        return root 
      return left if left else right
    
    
    
 def func(root,t):
  if not root:
    return 0
  
  def dfs(root,t):
    if not root:
      return 0
    res=0
    if root.val==t.val:
      res+=1
    dfs(root.left,t-root.val)
    dfs(root.right,t-root.val)
    
  
  ret=dfs(root,t)
  ret+=dfs()
  ret+=dfs()
  
 def func(root):
  res=0
  def dfs(root):
    if not root:
      return 0
    left=dfs(root.left)
    right=dfs(root.right)
    res=max(res,left+right+1)
    return max()+1
  
  

def func(root,p,q):
  
  def dfs(root,p,q):
    if not root:
      return 
    if root==p or root==q:
      return root
    left=dfs(root.left,p,q)
    right=dfs(root.right,p,q)
    
    if left and right:
      return root
    return left if left else right
  
  
 def func(nums):
  def helper(left,right):
    if left>right:
      return None
    mid=(left+right)//2
    root=TreeNode(nums[mid])
    root.left=dfs(root.left,left,mid-1)
    root.right=dfs(root.right,mid+1,right)
    
 
def func(root):
  pre=9999
  ans=9999
  def dfs(root):
    if not root:
      return 
    dfs(root.left)
    ans=min(ans,abs(ans-root.val))
    pre=root.val
    dfs(root.right)
  
  

 
def func(root,t):
  s=set()
  
  def dfs(root):
    nonlocal s
    if not root:
      return False
    if t-root.val in s:
      return True
    s.add(root.val)
    
    dfs(root.left)
    dfs(root.right)
    
    
def func(root):
  ans=[]
  pre=None
  count=0
  max_=0
  
  
  
  
def func(root):
  ans=[]
  max_=0
  count=0
  pre=None
  def dfs(root):
    if not root:
      return
    dfs(root.left)
    if root.val==pre:
      count+=1
    else:
      count=1
    if count==max_:
      ans.append(root.val)
    elif count>max_:
      max_count
      ans=[root.val]
    pre=root.val
    dfs()
    
    
def func(nums):
  if not nums:
    return 0
  q=[nums]
  visited=set()
  step=1
  while q:
    for i in range(len(q)):
      x=q.pop(0)
      for i in range(1,int(sqrt(nums))):
        t=x-i**2
        if t==0:
          return step
        elif t not in visited:
          visited.add(t)
          q.append(t)
    step+=1
    return step
          
          
      




    

  
  

    
      
    

    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
   
    
    
    
    
    
    
      
      
      
      
      
    
    
    
    
    
    
    
    
    
    
    
    
  
  
  
  
  
    

    
    
  
  
 


  
  
  
    
    
 
 


  
    
    
    
    
  
   

    

    
    
    
   
    

  
    
  
  

  

  
  
  

    
    
    
     

          
  





  
 
  



 
    
    
    
  
 

      


    
    


  
  
    
    
  
  

  
  
  
    
                
      
      
  

    
  

    
    
  

      


      
    
    

        
      
      
      
    
  
