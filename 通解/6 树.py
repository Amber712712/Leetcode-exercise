1 前中后序：dfs stack迭代
2 最大最小高度
3 相同树 对称树
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
    
      
    
    
    

                         
