1 查找单个数
def func(nums,target):
  l,r=0,len(nums)-1
  while l<=r:
    mid=(r-l)//2+l
    num=nums[mid]
    if num==target:
      return mid
    elif num>target:
      r=mid-1
    else:
      l=mid+1
  return -1
2 查找左边界/右边界
def left(nums,target):
  l,r=0,len(nums)-1
  while l<=r:
    mid=(r-l)//2+l
    
    if target>nums[mid]:
      l=mid+1
    elif target < nums[mid]:
      r=mid-1
    else:
      r=mid-1
 if nums[l]==target:
  return l
 else:
    return -1
  
def right(nums,t):
  
  
def func(nums):
  if not nums or len(nums)==0 or target<nums[0] or target>nums[-1]:
    return [-1,-1]
  lanser,ranswer=[self.left(nums,target),self.right(nums,target)]
  
  
    
3 查找极值点 nums[mid]>nums[mid-1] and  nums[mid]>nums[mid+1]
def func(nums):
  l,r=0,len(nums)-1
  while l<=r:
    mid=()//2+l
    if nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]:
      return mid
    elif nums[mid]>nums[mid+1]:
      r=mid-1
    else:
      l=mid+1
      
  return -1
