1 最短子序列和大于等于定
start end 指针 
首先移动end指针
def func(nums,target):
  start,end=0,0
  sum=0
  ans=len(nums)+1
  while end<len(nums):
    sum+=nums[end]
    while sum>target:
      ans=min(ans,end-start+1)
      sum-=nums[start]
      start+=1
    end+=1
  return 0 if ans==len(nums)-1 else ans
    
2 最长不重复的数列
abcdabc 最长为abcd
def func(s):
  if not s:
    return 0
  n=len(s)
  lookup=set()
  
  
  
  left=0
  curr_len=ans=0
  for i in range(n):
    curr_len+=1
    while s[i] in lookup:
      lookup.remove(s[left])
      left+=1
      curr_len-=1
    ans=max(ans,curr_len)
    lookup.add(s[i])
  return ans

3 
def func(s,target):
  if len(s)<len(target):
    return ""
  dic=collections.Counter(target)
  need=len(target)
  start,end=0,0
  min_len=len(s)+1
  ans1=0
  ans2=-1
  while end<len(s):
    if s[end] in dic:
      if dic[s[end]]>0:
        need-=1
      dic[s[end]]-=1
    while need==0:
      if end-start+1<min_len:
        ans2=end
        ans1=start
        
      if s[start] in dic:
        if dic[s[start]]>=0:
          need+=1
        dic[s[start]]+=1
        start+=1
    end+=1
  return s[ans1:ans2+1]
    
  
4 给你两个字符串 s1 和 s2 ，写一个函数来判断 s2 是否包含 s1 的排列。如果是，返回 true ；否则，返回 false

换句话说，s1 的排列之一是 s2 的 子串
要求滑动窗口是 固定长度 
def func(s1,t):
  if len(s1)<len(t):
    return []
  need=len(t)
  dic=collections.Counter(t)
  start,end=0,0
  n=len(s1)
  res=[]
  while end < n:
    if s1[end] in dic:
      if dic[s1[end]]>0:
        need-=1
      dic[s1[end]]-=1
      
    left=end-len(t)
    if left>0:
      if s1[left] in dic:
        if dic[s1[left]]>=0:
          need+=1
        dic[s1[left]]+=1
    if need==0:
      res.append(left)
        
       
    
      
        
    
 
  
  


      
   
    
        
        
      
      
        
    
    
  


