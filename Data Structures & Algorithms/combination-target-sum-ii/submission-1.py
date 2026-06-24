class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        n=len(nums)
        res=[]
        arr=[]
        nums.sort()
        def f(idx,target):
            if target==0:
                res.append(arr[:])
                return
            if idx==n:
                return
            if nums[idx]<=target:
                arr.append(nums[idx])
                f(idx+1,target-nums[idx])
                arr.pop()
            next_idx=idx+1
            while next_idx<n and nums[idx]==nums[next_idx]:
                next_idx+=1
            f(next_idx,target)
        f(0,target)
        return res

        