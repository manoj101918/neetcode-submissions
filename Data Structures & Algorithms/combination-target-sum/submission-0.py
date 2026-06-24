class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n=len(nums)
        res=[]
        arr=[]
        def f(idx,target):
            if target==0:
                res.append(arr[:])
                return
            if idx==n:
                return
            if nums[idx]<=target:
                arr.append(nums[idx])
                f(idx,target-nums[idx])
                arr.pop()
            f(idx+1,target)
        f(0,target)
        return res

        