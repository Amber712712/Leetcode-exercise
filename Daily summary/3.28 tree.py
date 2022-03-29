1 迭代法求前序，中序，后序
def func(root):
  stack=[root]
  res=[]
  while stack:
    n=stack.pop()
    res.append(n.val)
    if n.right:
      stack.append(n.right)
    if n.left:
      stack.append(n.left)
  return res
中：
def func(root):
  stack,res=[],[]
  
  def func(root):
    
    def dfs(root):
      if not root:
        return 0
      left=dfs(root.left)
      right=dfs(root.right)
      left=left+1 if root.val=root.left.val else0
      
  while root or stack:
    while root:
      stack.append(root)
      root=root.left
    tmp=stack.pop()
    res.append(tmp.val)
    root=tmp.right
    
后序：
与中序正好left,right相反 但是最后返回res[::-1]

2 非自顶而下：
相同节点值的最大路径
def func(root):
  self,ans=0
  def dfs(root):
    if not root:
      return 0
    left=dfs(root.left)
    right=dfs(root.right)
    if root.left:
      left=left+1 if root.val==root.left.val else 0
    if root.right:
      right=right+1 if root.val==root.right.val else 0
    self.ans=max(self.ans,left+right)
    return max(left,right)
  dfs(root)
  
  
3 
    
    

  
    
