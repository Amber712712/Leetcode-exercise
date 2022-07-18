找出链表交点：
def func(l1,l2):
  h1,h2=l1,l2
  while h1!=h2:
    if not h1:
      h1=l2
    else:
      h1=h1.next
    if not h2:
      h2=l1
    else:
      h2=h2.next
  return h1

链表反转
def func(head):
  cur,pre=head,None
  while cur:
    next_=cur.next
    cur.next=pre
    pre=cur
    cur=next_
  return pre

归并两个有序的链表
def func(head1,head2):
  if not head1:
    return head2
  if not head2:
    return head1
  if head1.val<head2.val:
    head1.next=func(head1.next,head2)
    return head1
  else:
    head2.next=func(head1,head2.next)
    return head2
迭代：
def func(head1,head2):
  if not head1 or not head2:
    return head1 if head1 else head2
  dummy=ListNode(0)
  tail=head
  p1,p2=head1,head2
  while p1 and p2:
    if p1.val<p2.val:
      tail.next=p1
      p1=p1.next
    else:
      tail.next=p2
      p2=p2.next
    tail=tail.next
  tail.next=head1 if head1 else head2
  return head.next

    
    

从有序链表中删除重复节点
def func(head):
  cur=head
  while cur.next:
    if cur.val==cur.next.val:
      cur.next=cur.next.next
    else:
      cur=cur.next
  return head
    
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
##将后面两个节点交换
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
def func(head):
  if not head:
    return True
  
  first_h=head
  first_end=mid(head) ##注意这里 需要翻转的需要从下一节点开始
  second_h=rev(first_end.next)
  
  
  res=True
  while res and second_h:
    if first_h.val!=second_h.val:
      res=False
    first_h=first_h.next
    second_h=second_h.next
    
  first_end.next=rev(second_h)
  def mid(head):
    s,f=head,head
    while f.next and f.next.next:
      s=s.next
      f=f.next.next
    return s
  
  def rev(head):
    cur=head
    pre=None
    while cur:
      next_=cur.next
      cur.next=pre
      pre=cur
      cur=next_
    return pre
  
    
5 分隔链表为K 个 每部分的长度都应该尽可能相同，排在前面的长度应该大于等于后面的
def splitListToParts(self, head: ListNode, k: int) -> List[ListNode]:
        n=0
        node=head
        while node:
            n+=1
            node=node.next
        b,q=n//k,n%k
        i=0
        curr=head
        ans=[None for _ in range(k)]
        while i < k and curr:
            ans[i]=curr
            l=b+(1 if i<q else 0)
            for _ in range(l-1):
                curr=curr.next
            next_=curr.next
            curr.next=None
            curr=next_
            i+=1
        return ans
      

6 链表元素按奇偶聚集
def func(head):
  if not head or head.next:
    return head
  odd,even=head,head.next
  while even or even.next:
    odd.next=even.next
    odd=odd.next
    even=odd.next
    even=even.next
  odd.next=head.next
  return head
  






    
  
    
    
    
    



  
