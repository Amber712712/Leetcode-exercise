1 平衡树
从下到上：从下到上判断 
新建方程：因为返回的是高度 如果返回的是-1 或者判断高度差大于2 则返回-1 否则返回高度
返回方程的值是否为-1

def func(root):
  def b(root):
    if not root:
      return 0
    l=b(root.left)
    r=b(root.right)
    if abs(l-r)>=2 or l==-1 or r==-1:
      return -1
    else:
      return max(l,r)+1
    
  return b(root)>=0

从上到下：
建立高度函数
判断每个节点高度差 
def func(root):
  if not root:
    return True
  if abs(height(root.left)-height(root.right))>=2:
    return False
  return func(root.left) and func(root.right)
  
def height(root):
  if not root:
    return 0
  return max(height(root.left),height(root.right))+1

2 路径之和为定值
bfs:
  def func(root):
    if not root:
      return False
    queue1=Collections.deque([root])
    queue2=Collections.deque([root.val])
    while queue1:
      node=queue1.popleft()
      val=queue2.popleft()
      


