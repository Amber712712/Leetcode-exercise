dfs: root.left+[]+root.right
  root.left->root.left.left+[]+root.left.right
1 前中后序：dfs stack迭代
https://leetcode-cn.com/problems/binary-tree-inorder-traversal/solution/python3-er-cha-shu-suo-you-bian-li-mo-ban-ji-zhi-s/
中序：
dfs:
  def func(root):
    if not root:
      return []
    return [root.val]+dfs(root.left)+dfs(root.right)
前序：
def func(root):
  if not root:
    return []
  return dfs(root.left)+[root.val]+dfs(root.right)


2 最大最小高度 (dfs和bfs)
最大高度：
def func(root):
  if not root:
    return 0
  return max(func(root.left),func(root.right))+1

def func(root):
  if not root:
    return 0
  queue=[root]
  step=0
  while queue:
    
    for i in range(len(queue)):
      r=queue.pop(0)
      if not root.left:
        queue.append(root.left)
      if not root.right:
        queue.append(root.right)
    step+=1
    
 return step
      

3 相同树 (dfs bfs)
dfs 
def func(root1,root2):
  if not root1 and not root2:
    return True
  if not root1 or not root2:
    return False
  if root1.val!=root2.val:
    return False
  
  return func(root1.left,root1.left) and func(root1.right,root2.right)

BFs:
  def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def BFS(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            queue1 = collections.deque()
            queue2 = collections.deque()
            queue1.append(p)
            queue2.append(q)
            while queue1 and queue2:
                node1 = queue1.popleft()
                node2 = queue2.popleft()
                # 如果都是空节点，跳过
                if not node1 and not node2:
                    continue 
                # 如果有一个为空，不可能相等，返回false
                if not node1 and node2 or not node2 and node1:
                    return False
                # 如果不为空，一定有值，若不相等，直接返回false。若相等，再后续添加节点
                if node1.val != node2.val:
                    return False
                queue1.append(node1.left)
                queue1.append(node1.right)
                queue2.append(node2.left)
                queue2.append(node2.right)
            # 如果还有节点没遍历完，则一定不等
            if queue1 or queue2:
                return False
            return True
        return BFS(p, q)


  
  

对称树
dfs 
def func(r1,r2):
  
4 平衡树（从上到下 从下到上）
def func(root):
  def h(root):
    if not root:
      return 0
    hl=h(root.left)
    hr=h(root.right)
    if abs(hl-hr)>1 or hl==-1 or hr==-1:   ###use if
      return -1
    else:
      return max(hl,hr)+1
 return h(root)>=0
 
 def func(root):
  def h(root):
    if not root:
      return 0
    return max()+1
  
  if not root:
    return true
  return abs(h(root.left)-h(root.right))<2 and func(root.left) and func(root.right)


5 路径之和为定值
def func(root):
  if not root:
    return False
  queue1=Collections.deque([root])
  queue2=Collections.deque([root.val])
  while 
  
def func(root,sum):
  if not root:
    return false
  if not root.left and root.right:
    return root.val==sum
  return func(root.left,sum-root.val) or func(root.right,sum-root.right)
6 翻转树
def func(root):
  if not root:
    return 0
  queue=[root]
  while queue:
    r=queue.pop(0)
    r.left,r.right=r.right,r.left
    if r.left:
      queue.append(r.left)
    if r.right:
      queue.qppend(r.right)
  return root

def func(root):
  if not root:
    return 0
  root.left,root.right=root.right,root.left
  func(root.left)
  func(root.right)
  return root

7 所有路径
BFS:
def func(root):
  if not root:
    return []
  l=list()
  quenode=Collections.deque([root])
  queval=Collections.deque([root.val])
  while queue:
    r=quenode.popleft()
    rv=queval.popleft()
    if not r.left and not r.right:
      l.append(queval)
    if r.left:
      quenode.append(r.left)
      queval.append(rv+'->'+str(r.left.val))
    if r.right:
      quenode.append(r.right)
      queval.append(rv+'->'+str(r.right.val))
      
  return queval
    
8 A树是否包含B树
BFS
def func(a,b):
  def help(a,b):
    queue=[(a,b)]
    while queue:
      a,b=queue.pop(0)
      if not a or a.val!=b.val:   ####限制范围是a树历遍完或者两值不同
        return False
      if b.left:
        queue.append(b.left)
      if b.right:
        queue.append(b.right)
    return True
  
  if not b:
    return False
  queuea=collections.deque([a])
  while queuea:
    node=queuea.pop(0)
    if node.val==b.val:
      if help(node,b):
        return True
    if node.left:
      queuea.append(node.left)
    if ndoe.right:
      queuea.append(node.right)
  return False
9 是否包含子树
def func(a,b):
  if not a and not b:
    return True
  if not a or not b:
    return False
  return func(a,b) or func(a.left,b.left) or func(a.right,b.right)  ##从开头开始dfs

  
  def dfs(a,b):
    if not a and not b:
      return True
    if not a or not b:
      return False
    if a.val!=b.val:
      return False
    return dfs(a.left,b.left) and dfs(a.right,b.right)
      
10 左叶子之和
BFS：
def func(root):
  if not root:
    return 0
  res=0
  isleft=lambda node not node.left and nort node.right
  q=collections.deque([root])
  while q:
    r=q.popleft()
    if r.left:
      if isleft(r.left):
        res+=r.left.val
      else:
      q.append(r.left)
    if r.right:
      q.append(r.right)
      
11 填充二叉树节点的右侧指针
dfs:
  def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        self.dfs(root.left,root.right)
        return root

    def dfs(self,node1,node2):
        if not node1 or not node2:
            return None
        node1.next=node2
        self.dfs(node1.left,node1.right)
        self.dfs(node2.left,node2.right)
        self.dfs(node1.right,node2.left)
Bfs:
  def func(root):
    if not root:
      return None
    queue=collections.deque([root])
    while queue:
      for i in range(len(queue)):
        r=queue.pop(0)
        for i <len(queue)-1:
          r.next=queue[0]
        
        if r.left:
          queue.append(r.left)
        if r.right:
          queue.append(r.right)
          
      
 
    
    
    

                         
