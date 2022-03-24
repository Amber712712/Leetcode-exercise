总结：
翻转树：
不用判断左右子叶是否存在 直接交换 前序遍历或后序遍历
层序遍历一样吧补判断左右是否存在

合并树：
1 创造新树 new=TreeNode(n1.val+n2.val) new.left=   new.right=  return new
2 层序遍历 
判断两节点是否都存在：
   存在：
     建立新node
    
三个root node 入queue
while root1 and root2:
  pop
  if root1.left or root2.left:
    三种情况
    
  if root1.right or root2.right:
    三种情况
    
3 路径之和为定值
dfs :
  
bfs:
  sum和node同时入queue
 
4 路径之和问题 不一定从头开始在尾结束
dfs:
  def func(root):
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
    ret=dfs(root.t)
    ret+=func(root.left,t)
    ret+=func(root.right,t)
    return ret
  
  
  
  
1 翻转树
dfs
前序 翻转：
def func(root):
  if not root:
    return root
  root.left,root.rght=root.right,root.left
  func(root.left)
  func(root.right)
  return root
后序翻转：
def func(root):
  if not root:
    return root
  left=func(root.left)
  right=func(root.right)
  root.left,root.right=left,right
  return root

层序翻转：
在交换时不需要判断root.left root.right是否存在
使用queue交换的机制是利用queue遍历
def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        q=collections.deque([root])
        while q:
            for i in range(len(q)):
                node=q.popleft()
                node.left,node.right=node.right,node.left
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return root
      
  
2 合并二叉树 #创建新树的过程 
前序：
dfs
def func(root1,root2):
  if not root1 and not root2:
            return None
        if not root1:
            return root2
        if not root2:
            return root1
        new=TreeNode(root1.val+root2.val)
        new.left=self.mergeTrees(root1.left,root2.left)
        new.right=self.mergeTrees(root1.right,root2.right)
        return new
      
层序：
def func(root1,root2):
  if not root1 and not root2:
            return None
  if not root1:
            return root2
  if not root2:
    return root1
  new=TreeNode(root1.val+root2.val)
  q,q1,q2=[new],[root1],[root2]
  while q1 and q2:
    n,n1,n2=q.pop(0),q1.pop(0),q2.pop(0)
    if n1.left or n2.left:
      if n1.left and n2.left:
        n.left=TreeNode(n1.left.val+n2.left.val)
        q.append(n.left)
        q1.append(n1.left)
        q2.append(n2.left)
      if n1.left:
        n.left=n1.left
      if n2.left:
        n.left=n2.left
    
    if n1.right or n2.right:
      if n1.right and n2.right:
        n.right=TreeNode(n1.right.val+n2.right.val)
        q.append()
        q1.append()
        q2.append()
      if n1.right:
        n.right=n1.right
      if n2.right:
        n.right=n2.right
   return new

3 判断路径之和为定值
dfs
def func(root,t):
  if not root:
    return False
  if not root.left and not root.right:
    return root.val==t
  return func(root.left,t-root.val) or func(root.right,t-root.val)
BFS:
  def func(root,t):
    if not root:
      return False
    q,q_val=[root],[root.val]
    while q:
      node,val=q.pop(0),q_val.pop(0)
      if not node.left and not node.right:
        if val==t:
          return True
        
      if node.left:
        q.append(node.left)
        q_val.append(val+node.left.val)
      if node.right:
        q.append(node.right)
        q_val.append(val+node.right.val)
     return False
  
 4 统计路径和等于一个数的路径数量  路径不一定以 root 开头，也不一定以 leaf 结尾，但是必须连续。
dfs
分为两部分 
第一部分：建立方程计算根为root的符合条件的个数  第二部分：从上到下遍历树 计算和
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
  ret+=func(root.left,t)
  ret+=func(root.right,t)
  return ret
  
 
前缀和：算法思想 
num 
sum=[0]*(len(nums)+1) 长度为n+1
for i in range(0,len(nums)):  从0开始
  sum[i+1]=sum[i]+nums[i]
  
  
  



    
    
      
    
    
  
        
        
 
        
      
    
  
    
