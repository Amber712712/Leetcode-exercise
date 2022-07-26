1 
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




