1 删除链表的倒数第 n 个节点：重点是找出倒数第N的节点
快慢指针
def func(head):
  dummy=ListNode(0,head)
  fast=head
  slow=dummy
  for i in range(n):
    fast=fast.next
  while fast:
    fast=fast.next
    slow=slow.next
  slow.next=slow.next.next
  return dummy.next
可以入栈：借助stack 找出倒数第N的节点
def func(head):
  stack=[]
  dummy=ListNode(0,head)
  curr=dummy
  while curr:
    stack.append(curr)
    curr=curr.next
  for i in range(n):
    stack.pop()
  pre=stack[-1]
  pre.next=pre.next.next
  return dummy.next
2 交换链表中的相邻结点
def func(head):
  dummy=ListNode(0)
  dummy.next=head
  curr=dummy
  while curr.next and curr.next.next: ##保证后面至少有2节点
    node1=curr.next 
    node2=curr.next.next
    curr.next=node2 #保证开头找到
    node1.next=node2.next
    node2.next=node1
    curr=node1
  return dummy.next


3 链表求和 不能翻转链表 使用栈
def func(l1,l2):
  s1=list()
  s2=list()
  while l1:
    s1.append(l1.val)
    l1=l1.next
  while l2:
    s2.append(l2.val)
    l2=l2.next
  carry=0
  ans=None
  while s1 or s2 or carry:
    a=0 if not s1.pop() else s1.pop()
    b=0 if not s2.pop() else s2.pop()
    cur=a+b+carry
    
    carry=cur//=10 ##上一个进数
    cur%=10 ##余数
    curnode=ListNode(cur)  #将新的节点加在旧节点前面
    curnode.next=ans
    ans=curnode
  return ans
    

4 回文链表
使得空间为O（1）的话 将后半部分翻转与前半部分比较


    
  
    
    
    
    



  
