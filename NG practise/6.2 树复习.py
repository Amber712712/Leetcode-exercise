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
      
2 
