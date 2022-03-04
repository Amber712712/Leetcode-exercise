高度有关：
1 二叉树最大直径（子树 需要用后序）
def func(self, root):
  self.ans=1
  def dfs(root):
    if not root:
      return 0
    l=dfs(root.left)
    r=dfs(root.right)
    self.ans=max(self.ans,l+r+1)
    return max(l,r)+1
  dfs(root)
  return self.ans-1

2 最大高度 (后序排列)
def func(root):
  if not root:
    return 0
  return max(func(root.left),func(root.right))+1
  
3 前中后序遍历
前序：
#1 递归1
def func(root):
  if not root:
    return None
  return [root.val]+func(root.left)+func(root.right)
#2 递归2
def func(self,root):
  if not root:
    return []
  res=[]
  self.dfs(root,res)
  return res
  
def dfs(self,root,res):
  if not root:
    return None
  res.append(root.val)
  dfs(root.left,res)
  dfs(root.right,res)
  
#3 迭代

4 翻转二叉树（前序后序都行）
def func(root):
  if not root:
    return root
  root.left,root.right=root.right,root.left
  func(root.left)
  func(root.right)
  
  return root

5 填充二叉树节点的右侧指针(dfs bfs)
dfs
def func(root):
  
  
  



  
