1 修剪二叉查找树  L R
def func(root,L,R):
if not root:
            return None
        if root.val<L:
            return self.trimBST(root.right,L,R)
        if root.val>R:
            return self.trimBST(root.left,L,R)
        root.left=self.trimBST(root.left,L,R)
        root.right=self.trimBST(root.right,L,R)

        return root
      
 

2 寻找二叉查找树的第 k 个元素
230. Kth Smallest Element in a BST 
中序遍历 使用dfs 迭代
迭代
def func(root,k):
  if not root:
    return None
  stack=[]
  while stack or root:
    while root:
      stack.append(root)
      root=root.left
    val=stack.pop()
    k-=1
    if k==0:
      return val
    root=root.right
    
   
def func(root,k):
  res=[]
  def dfs(root):
    nonlocal res
    if not root:
      return 
    dfs(root.left)
    res.append(root.val)
    dfs(root.right)
  dfs(root)
  return res[k-1]
       
  
 3 把二叉查找树每个节点的值都加上比它大的节点的值
利用中序的升序结构
反向中序遍历 降序 并逐渐加和付给节点
DFS
def func(root):
  ans=0
  def dfs(root):
    nonlocal ans
    if not root:
      return None
    dfs(root.right)
    ans+=root.val
    root.val=ans
    dfs(root.left)
    
  dfs(root)
  return root

4 二叉搜索树公共祖先 （题干是一定可以找到）
卡两个值的中间值
递归
def func(root,p,q):
  if p<root.val and q<root.val:
    return func(root.left,p,q)
  elif p>root.val and q>root.val:
    return func(root.right,p,q)
  return root

迭代
def func(root,p,q):
  pointer=root
  if not root:
    return root
  if p<root.val and q<root.val:
    pointer=root.left
  elif p>root.val and q>root.val:
    pointer=root.right
  return pointer
    
5 二叉树公共祖先
dfs
def func(root,p,q):
  def dfs(root,p,q)
  if not root:
    return None
  if root.val==p.val or root.val==q.val:
    return root.val
  left=dfs(root.left,p,q)
  right=dfs(root.right,p,q)
  
  if left and right:
    return root
  return left if left else right






    


  
  

  







  
 
    
  
