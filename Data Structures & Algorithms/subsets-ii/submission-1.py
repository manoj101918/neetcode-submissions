class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        arr=[]
        res=[]
        nums.sort()

        def f(idx):
            if idx==n:
                res.append(arr[:])
                return 
            arr.append(nums[idx])
            f(idx+1)
            arr.pop()
            nex_idx=idx+1
            while nex_idx<n and nums[idx]==nums[nex_idx]:
                nex_idx+=1
            
            f(nex_idx)
        f(0)
        return res