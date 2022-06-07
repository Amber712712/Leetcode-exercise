1 对称树 O（n）O(n)
BFS：
def func(root):
  if not root:
    return True
  queue=collections.deque()
  queue.append((root.left,root.right))
  while queue:
    for i in range(len(queue)):
    l,r=queue.popleft()
    if not l and not r:
      continue
    if not l or not r:
      return False
    if l.val!=r.val:
      return False
    queue.append((l.left,r.right))
    queue.append((l.right,r.left))
  return True
#用转码方法 层序遍历
def func(root):
  if not root:
    return False
  queue=deque()
  deque.append(root)
  while queue:
    s=''
    for i in range(len(queue)):
      
      node=queue.popleft()
      if not node:
        s+=" "
      else:
        s+=chr(node.val)
        queue.append(node.left)
        queue.append(node.right)
    if s!=s[::-1]: #注意层序遍历
       return False
    return True
   

DFS:
  def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        return self.func(root.left,root.right)
    
    def func(self,left,right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.val!=right.val:
            return False
        return self.func(left.left,right.right) and self.func(left.right, right.left)
      
*2 （树包含问题：是否有一条路径与所给的结构相同）子结构/子树包含/树内是否包含列表 问题  a包含b结构
子树；
到达节点后 判断子树 
dfs:
  def check(roota,rootb):
    if not 
子结构：
到达节点后 判断子结构
时间复杂度：O（mn）

bfs:
  def func(roota,rootb):
    queue=deque()
    queue.append((roota,rootb))
    while queue:
      a,b=queue.popleft()
      if not a or a.val!=b.val:
        return False
      if b.left:
        queue.append((a.left,b.left))
      if b.right:
        queue.append((a.right,b.right))
     return True
  
   def final(roota,rootb):
      if not roota:
        return False
      queue=deque(roota)
      while queue:
        a=queue.popleft()
        if a.val==rootb.val:
          if func(a,rootb):
            return True
        if a.left:
          queue.append(a.left)
        if a.right:
          queue.append(a.right)
       return False
    
DFS:
  def func(roota,rootb):
    if not rootb: ####注意这里把B遍历完后返回True
      return True
    if not roota or roota.val!=rootb.val:
      return False
    return func(roota.left,rootb.left) and func(roota.right,rootb.right)
  def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if not A or not B:
            return False
        return self.check(A,B) or self.isSubStructure(A.left,B) or self.isSubStructure(A.right,B)
      
列表：head

3 二叉树最大直径
def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans=0
        def dfs(root):
            if not root:
                return 0
            left=dfs(root.left)
            right=dfs(root.right)
            self.ans=max(left+right,self.ans)
            return max(left,right)+1
        dfs(root)
        return self.ans

高度：
BFS：
def func(root):
  if not root:
    return 0
  queue=[root]
  while queue:
    ans=0
    for i in range(len(queue)):
      q=queue.pop(0)
      if q.left:
        queue.append(q.left)
      if q.right:
        queue.append(q.right)
    
4 左指针指向右指针
BFS：
while queue:
  for i in range(len(queue)):
    q=queue.popleft()
    q.next=queue[0]
    if q.left:
    if q.right:
      
return root

DFS：
def func(root):
  if not root:
    return root
  dfs(root.left,root.right)
  return root
  
def dfs(left,right):
  if not left or not right:
    return 
  left.next=right
  dfs(left.left,left.rgiht)
  dfs(right.left,right.right)
  dfs(left.right,right.left)
  
  
5 翻转二叉树
pre-order and post-order
def dfs(root):
  if not root:
    return
  left=dfs(root.left)
  right=dfs(root.right)
  root.left,root.right=right,left
  return root

root.left,root.right=root.right,root.left
dfs(root.left)
dfs(root.right)
return root

iteration:
  while queue:
    q=queue.popleft()
    q.left,q.right=q.right,q.left
    if q.left:
    
    if q.right:
      
      

6 平衡树 
pre-order
def dfs(root):
  if not root:
    return True
  if abs(height(root.left)-height(root.right))>=2:
    return False
  return dfs(root.left) and dfs(root.right)

  
def height(root):
  if not root:
    return 0
  return max(height(root.left),height(root.right))+1

post-order:
  def dfs(root):
    if not root:
      return True
    left=dfs(root.left)
    right=dfs(root.right)
    if abs(left-right)>=2 or left==-1 or right==-1:
      return -1
    return max(left,right)+1
  return dfs(root)!=-1


7 路径之和为定值
target sum I
DFS:
  def func(root,t):
    if not root:
      return False
    if not root.left and not root.right and root.val==t:
      return True
    return func(root.left,t-root.val) or func(root.right,t-root.val)
  
 * target sum II:使用回溯法 利用path 和 paths 
  dfs1：
  def func(root,t):
    res=[]
    path=[]
    def dfs(root,t):
      if not root:
        return 0
      path.append(root.val)
      if not root.left and not root.right and root.val==t:
        res.append(path)
      dfs(root.left,t-root.val)
      dfs(root.right,t-root.val)
      path.pop()
    dfs(root,t)
    return res
  dfs2:
    def func(root,t):
      res=[]
      def dfs(root,t,res,path):
        if not root:
          return
        if not root.left and not root.right and root.val==t:
          res.append(path+[root.val])
        dfs()
        dfs()
      return res
    
 bfs:
   def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res=[]
        que=[(root,[],0)]
        while que:
            node,path,s=que.pop(0)
            if not node:
                continue
            if not node.left and not node.right and s+node.val==targetSum:
                res.append(path+[node.val])
            que.append((node.left,path+[node.val],s+node.val))
            que.append((node.right,path+[node.val],s+node.val))
        return res
      
 
 target sum III:
  dfs:
    def func(root,t):
      
      def dfs(root,t):
        if not root:
          return 0
        ans=0
        if root.val==t:
          ans+=1
        ans+=dfs(root.left,t-root.val)
        ans+=dfs(root.right,t-root.val)
        return ans
      ret=dfs(root,t)
      ret+=func(root.left,t)
      ret+=func(root.right,t)
      return ret
  pre-sum method:
    def func(root,t):
      prefix=collections.defaultdict(int)
      prefix[0]=1
      def dfs(root,curr):
        if not root:
          return 0
        ret=0
        
        

      
    
   
    
    
    
    



      


   



 
  
  
  



    
    
    
       

