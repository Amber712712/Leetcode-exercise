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
  while root or stack:
    while root:
      stack.append(root)
      root=root.left
    tmp=stack.pop()
    res.append(tmp.val)
    root=tmp.right
    
后序：
与中序正好left,right相反 但是最后返回res[::-1]

  
    
