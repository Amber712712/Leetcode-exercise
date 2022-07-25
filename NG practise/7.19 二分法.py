二分查找基础
二分查找左右边界
旋转数组/+有重复值
随意找出一座山峰顶端
二维有序矩阵查找

1 二分法查找
def func(nums,k):
  l,r=0,len(nums)
  while l<=r:
    mid=()//2
    if nums[mid]==k:
      return mid
    elif 
    
2 查找左右边界
3 旋转数组中找出target:
  首先先确定哪一半是升序或降序
  在一定顺序的一半进行二分操作
  def func(nums,k):
    l,r=0,len(nums)-1
    while l<=r:
      mid=(l+r)//2
      if nums[mid]==k:
        return mid
      if nums[l]<=nums[mid]:
        if nums[l]<=k<nums[mid]:
          r=mid-1
        else:
          l=mid+1
      else:
        if nums[mid]<k<=nums[r]:
          l=mid+1
        else:
          r=mid-1
          
旋转数组中有重复的值 如果num[l]==nums[mid]==nums[r] 则两边缩紧 剩下步骤与上面相同
 if not nums:
            return False
        
        n = len(nums)
        if n == 1:
            return nums[0] == target
        
        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return True
            if nums[l] == nums[mid] and nums[mid] == nums[r]:
                l += 1
                r -= 1
            elif nums[l] <= nums[mid]:
                if nums[l] <= target and target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        
        return False


4 山峰顶端
答案左边为nums[mid-1]<nums[mid] 右边则nums[mid]>nums[mid+1]
def func(nums):
   n = len(arr)
        left, right, ans = 1, n - 2, 0

        while left <= right:
            mid = (left + right) // 2
            if arr[mid] > arr[mid + 1]:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return ans
      
随意返回山顶顶端的点
def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)

        # 辅助函数，输入下标 i，返回 nums[i] 的值
        # 方便处理 nums[-1] 以及 nums[n] 的边界情况
        def get(i: int) -> int:
            if i == -1 or i == n:
                return float('-inf')
            return nums[i]
        
        left, right, ans = 0, n - 1, -1
        while left <= right:
            mid = (left + right) // 2
            if get(mid - 1) < get(mid) > get(mid + 1):
                ans = mid
                break
            if get(mid) < get(mid + 1):
                left = mid + 1
            else:
                right = mid - 1
        
        return ans
5 二维矩阵的查找 全程升序
def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r, c = len(matrix), len(matrix[0])
        i, j = 0, r*c-1
        while i <= j:
            m = (i+j)//2
            val = matrix[m//c][m%c]  ###一维数组中的m th 对应矩阵matrix[m//c][m%c]
            if val > target: j = m-1
            elif val < target: i = m + 1
            else: return True
        return False

      
      
      


    
