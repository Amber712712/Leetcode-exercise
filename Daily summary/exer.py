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
        
      
      
      
    
  
