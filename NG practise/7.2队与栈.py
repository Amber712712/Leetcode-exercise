1 用栈实现队列
class MyQueue(object):
  def _init_(self):
    self.s1=[]
    self.s2=[]
  def push(self,x):
    self.s1.append(x)
  def pop(self):
    if not self.s2:
      while self.s1:
        self.s2.append(self.s1.pop())
    return self.s2.pop()
  def peek(self):
    if not self.s2:
      while self.s1:
        self.s2.append(self.s1.pop())
    return self.s2[-1]
  def empty(self):
    return not self.s1 and not self.s2
  
2 用队列实现栈
class MyStack:
  def _init_(self):
    self.q1,self.q2=collections.deque(),collections.deque()
  def push(self,x):
    self.q2.append(x)
    while q1:
      self.q2.append(self.q1.popleft)
    self.q1,self.q2=self.q2,self.q1
  def pop(self):
    return self.q1.popleft
  def top(self):
    return self.q1[0]
  def empty:
    return not self.s1
 
3 最小值栈 利用辅助栈/一个栈同时存储最小值
class MinStack:
  def _init_(self):
    self.s1=[]
  def push(self,x):
    if not self.s1:
      self.s1.append((x,x))
    else:
      self.s1.append((x,min(x,self.s1[-1][1])))
  def pop(self):
    return self.s1.pop()
  def getmin(self):
    return self.s1[-1][1]
  
4 用栈实现括号匹配
def func(s):
  if len(s)%2==1:
    return False
  stack=[]
  pairs={"]"="[",")"="("}
  for char in s:
    if stack and char in pairs and stack[-1]==pairs[char]: ##注意stack为空的时候
      stack.pop()
    else:
      stack.append(char)
  return stack==[]
   
  
5 数组中元素与下一个比它大的元素之间的距离 单调栈 
创造stack不断加入元素的index 当有元素比顶端大的时候 dic[nums[stack.pop()]]=nums[i]
剩下的栈内从上往下为升序


def func(nums):
  if not nums:
    return []
  stack=[]##放入的是index
  ans=[0*len(nums)]
  for i in range(len(nums)):
    while stack and nums[i]>nums[stack[-1]]:
      pre_i=stack.pop()
      ans[pre_i]=i-pre_i

    stack.append(i)
    

  
  
6 循环数组中比当前元素大的下一个元素 单调栈+循环数组 len(nums)*2
def func(nums):
  stack=[]
  res=[-1*len(nums)]
  for i in range(len(nums)*2):
    while stack and nums[stack[-1]]<nums[i%len(nums)]:
    
      res[stack.pop()]=nums[i%len(nums)]
    stack.append(i%len(nums))
    
   return res




      
  
  
  





  
  


        
