1 两数相加：
def func(l1,l2):
  dummy=p=ListNode(None) # 创建一个结点值为 None 的头结点, dummy 和 p 指向头结点, dummy 用来最后返回, p 用来遍历
  s=0
  while l1 or l2 or s:
    s+=(l1.val if l1 else 0)+(l2.val if l2 else 0)+s
    p.next=ListNode(s%10)
    p=p.next
    s//=10
    l1-l1.next if l1 else0
    l2=l2.next if l2 else 0
    
    
  
