1 337. House Robber III (Medium) 间隔遍历 用到递归+动态规划

def func(root):
  return max(dfs(root))  ###返回偷和不偷最大值

def dfs(root):
  if not root:
    return [0,0]
  left=dfs(root.left)
  right=dfs(root.right)
  s=root.val+left[1]+right[1]   #偷的话包含root值以及不能偷左右树
  nons=max(left)+max(right)     #不偷的话需要去取左右最大值相加和
  
  return [s,nons]


2 二叉树第二小的值 前提一个节点要么具有 0 个或 2 个子节点，如果有子节点，那么根节点是最小的节点
第二小的值需要定义一个最大值然后不断刷新最大值
用dfs 和 bfs进行遍历更新最大值

BFS
def func(root):
  q=[root]
  s1=root.val
  s2=2**31
  found=False
  while q:
    n=q.pop(0)
    if n.val>s1 and n.val<s2:
      s2=n.val
      found=True
      continue
    if n.left:
      q.append(n.left)
    if n.right:
      q.append(n.right)

DFS
def func(root):
  res=float('inf')
  minval=root.val
  def dfs(node):
    nonlocal res
    if not node:
      return None
    if node.val==minval:
      dfs(root.left)
      dfs(root.right)
    if minval<node.val<res:
      res=node.val
      
  dfs(root)
  return res if res!=float('inf') else -1
      
    


  


      
      


  
  
  

  
