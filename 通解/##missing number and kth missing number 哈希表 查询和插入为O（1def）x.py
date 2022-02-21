def func(nums):
    s=set(nums)####哈希表
    for i in range(len(nums)+1):
        if i not in s:
           return i
           

def func(arr,k):
    l=[i for i in range(arr[-1]+k+1)]  ###补0使得后面的引索值
    
