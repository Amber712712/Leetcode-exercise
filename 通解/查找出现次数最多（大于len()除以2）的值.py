1 字典
def func(nums):
  dict=collections.Counter(nums)
  return max(dict.key(), key=dict.get)

2 排序
def func(nums):
  nums.sort()
  return nums[len(nums)//2]  ###中位数

