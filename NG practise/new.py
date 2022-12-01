乘积小于k
def func(nums):
  if k==0 or k==1:
    return 0
  start,end=0,0
  mul=1
  res=0
  while end<len(nums):
    mul*=nums[end]
    
    while mul>=k:
      mul/=nums[start]
      start+=1
      
    res+=j-i+1
    
  return res


符合pattern的数组
4，3，2，5，4
def func(nums):
  start,end=0,0
  res=0
  while end<len(nums)-1:
    while nums[end]==nums[end+1]+1:
      end+=1
      
    while start<end:
      res+=end-start
      start+=1
    end+=1
    start=end
  return res


将数列中连续/其他pattern的数组取出
def func(nums):
  n=len(nums)
  i=0
  count=1
  res=[]
  while i<n-1:
    if nums[i]==nums[i+1]-1:
      count+=1
      
    else:
      res.append(nums[i:i+count])
      count=1
      
  res.append(nums[i+1-count:n])
  return res

重复出现k次的序列
def func(s):
  dic=collections.defaultdict()
  
  for i in range(len(s)-k+1):
    c=s[i:i+10]
    dic[c]=dic.get(c,0)+1
    
    if dic[c]==2:
      res.append(c)
      
出现重复元素
def func(nums,k):
  s=set()
  for i in range(len(nums)):
    if i>=k:
      s.remove(nums[i-k])
    if nums[i] in s:
      return True
    
    

  
  
      
    
        
       
