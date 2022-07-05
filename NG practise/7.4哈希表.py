1 最长和谐序列
def func(nums):
  dic={}
  for num in nums:
    dic[num]=dic.get(num,0)+1
  
  ans=0
  for num in nums:
    if num+1 in dic:
      ans=max(ans,dic[num]+dic[num+1]) #确定一边
      
2 最长连续序列
动态规划
def func(nums):
  if not nums:
    return 0
  dic={}
  max_=0
  for num in nums:
    if num not in dic:
      left=dic.get(num-1,0)
      right=dic.get(num+1,0)
      length=left+right+1
      
      max_=max(max_,length)
    
      dic[num]=1
      dic[num-left]=dic[num+right]=length
      
   return max_

确定lower bound:
def func(nums):
  s=set()
  for num in nums:
    s.add(num)
  ans=0
  
  for num in nums:
    if num-1 not in s:
      curr=num
      curr_len=1
    while curr+1 in s:
      curr_len+=1
      curr=num
    ans=max(ans,curr_len)
    
   return ans


    
      
      



      
    

  

    
   

