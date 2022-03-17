1 对称树 
注意用deque append ((root.left,root.right)) 包含在一起 同时一起popleft()
deque 不能用pop(0)
BFS：
def func(root):
  if not root:
            return True
        queue=collections.deque()
        queue.append((root.left,root.right))
       
        while queue:
            for i in range(len(queue)):
                left,right=queue.popleft()
                
                if not left and not right:
                    continue
                if not left or not right:
                    return False
                if left.val!=right.val:
                    return False
                queue.append((left.left,right.right))
                queue.append((left.right,right.left))
      
        return True 
 DFS:
  def func(root):
    
    def func1(left,right):
      
2 包含子树 A是否包含B结构
1 A是否包含B ：
将B遍历入queue   
在A不存在或A B 值不同时返回false 
2 寻找到A树和B树值相同的节点
bfs；
def func(roota,rootb):
  def bfs(a,b):
    queue=deque()
    queue.append((a,b))
    while queue:
      a,b=queue.popleft()
      if not a or a.val!=b.val:
        return False
      if b.left:
        queue.append((a.left,b.left))
      if b.right:
        queue.append((a.right,b.right))
        
    return True
  
  if not b:
    return False
  queue1=[a]
  while queue1:
    a=queue1.pop(0)
    if a.val=b.val:
      if bfs(a,b):
        return True
      
  return False
      
3 二叉树直径问题
return 的东西是每个节点的值
return max(left,right)+1  代表树的左右树最高高度（节点数）
使用全局变量使得
dfs:
  def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans=0
        def dfs(root):
            if not root:
                return 0
            left=dfs(root.left)
            right=dfs(root.right)
            self.ans=max(self.ans,left+right)
            return max(left,right)+1

        dfs(root)
        return self.ans
      
4 左指针指向右指针
在层序遍历i < len(queue)-1的时候，queue pop出的结果可以直接指向queue的第一位 queue[0]

BFS:
def func(root):
  if not root:
    return root
  queue=[root]
  while queue:
    for i in range(len(queue)):
      node=queue.pop(0)
      if i < len(queue)-1:
        node.next=queue[0]
      if node.left:
        queue.append(node.left)
      if node.right:
        queue.append(node.right)
      
  return root

DFS：


  

  

  
  
  


 
      
  
