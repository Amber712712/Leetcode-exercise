1 从有序数组中构造二叉查找树
def func(nums):
  
  def helper(left,right):
    if left>right:
      return
    mid==(left+right)//2
    root=TreeNode(nums[mid])
    root.left=dfs(left,mid-1)
    root.right=dfs(mid+1,right)
  return root
    
  return helper(0,len(nums)-1)

2 根据有序链表构造平衡的二叉查找树
首先确定链表中点 使用快慢指针 在使用中序遍历

def func(head):
  
  def mid(head,tail):
    slow=fast=head
    while fast!=tail or fast.next!=tail:
      slow=slow.next
      fast=fast.next.next
      
    return slow
  
  def dfs(head,tail):
    if head==tail:
      return 
    node=mid(head,tail)
    root=TreeNode(node.val)
    root.left=dfs(head,node)
    root.right=dfs(node.next,tail)
    return root
  
  return dfs(head,None)

3 在二叉查找树中寻找两个节点，使它们的和为一个给定值
def func(root,k):
  s=set()
  def dfs(root,k):
    if not root:
      return False
    if k-root.val in s:
      return True
    s.add(root.val)
    
    
4 寻找二叉查找树中出现次数最多的值
空间复杂度为O（1） 中序遍历 有顺序的遍历 
def func(root):
  ans=[]
  count=0
  max_=0
  pre=None
  def dfs(root):
    if not root:
      return 
    dfs(root.left)
    if pre==root.val:
      count+=1
    else:
      count=1
    if max_==count:
      ans.append(root.val)
    elif count>max_:
      ans=[root.val]
      max_=count
    pre=root.val
    dfs(root.right)
    
  dfs(root)
  return ans


    
      
      
      
      
      
      
      
      
      
      
      
      
      
      

    
    
    
    
   

    
    
    
    
  
  
  
  
  
  
  
  
  






    
  

   
  

    
  
  
  
