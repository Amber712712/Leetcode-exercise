
1 长度最小的数组
利用前缀和+二分法 二分法查找右边界：符合条件的最右边的数字 
延申：递增数组中，找到差值小于等于某值的最右边的数字
def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if not nums:
            return 0
        pre=[0]
        for i in range(len(nums)):
            pre.append(pre[-1]+nums[i])
        
        l,r=0,len(pre)
        res=float('inf')
        mid=-1
        for i in range(len(pre)):
            d=pre[i]-target
            if d<0:
                continue
            l=0
            r=i
            while l<=r:
                mid=(l+r)//2
                if pre[mid]<=d:
                    ans=mid
                    l=mid+1
                else:
                    r=mid-1
            res=min(res,i-ans)
        if mid==-1:
            return 0
        else:
            return res
          
2 
