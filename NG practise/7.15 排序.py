
1 大根堆/小根堆
数组中第K大的元素
def func(nums):
  heap=[]
  for num in nums:
    heapq.heappush(heap,num)
    if len(heap)>k:
      heapq.heappop(heap)
  return heap[0]


def func(nums,k):
  heap=nums
  heapq.heapify(heap)
  n=len(nums)
  for i in range(n-k):
    heapq.heappop(heap)
  return heap[0]

