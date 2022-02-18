1 冒泡排序
def func(nums):
  for i in range(len(nums)-1):
    for j in range(0,len(nums)-1):
      if nums[j]>nums[j+1]:
        换位置


2 选择排序
def func(nums):
  for i in range(len(nums)-1):
    minindex=i
    for j in range(i+1,len(nums)):
      if nums[j]<nums[minindex]:
        minindex=j
    if minindex!=i:####遍历完确定最小值位置
       nums[i],nums[minindex]=nums[minindex],nums[i]
     
      


3 
