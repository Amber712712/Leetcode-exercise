对称树 
知识点 
1 可以用ASCII码 来进行回文判断
2 可以将root.left root.right同时入队列

1 统计左叶子节点的和
dfs
分两部分 第一判断是否为左子叶 第二加和

    
def func(root):
  if not root:
    return 0
  res=0
  if root.left and not root.left.left and not root.left.right:
    res+=root.left.val
  return func(root.left) + func(root.right)

2 填充右指针
注意层序遍历时利用的是i的值
def func(root):
  if not root:
    return root
  q=[root]
  while q:
    for i in range(len(q)): #####注意
      n=q.pop(0)
      if i<len(q)-1:
        n.next=q[0]
      if n.left:
        q.append(n.left)
      if n.right:
        
        
def func(root):
  if not root:
    return root
  func1(root.left,root.right)
  return root
  
def func1(l,r):
  if not l or not r:
    return None
  l.next=r
  func(l.left,l.right)
  func(r.left,r.right)
  func(l.right,r.left)
  
 3 将树拉伸为链表
注意是原地展开 不能创造新链表
分为两步 前序遍历入list+构造链结构（左树为空 右数指向下个数）
def func(root):
  l=list()
  def dfs(root):
    l.append(root)
    dfs(root.left)
    dfs(root.right)
    
  
  


      
  
    

    
