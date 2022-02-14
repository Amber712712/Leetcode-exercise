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


5 
