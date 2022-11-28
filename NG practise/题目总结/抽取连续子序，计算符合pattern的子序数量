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
