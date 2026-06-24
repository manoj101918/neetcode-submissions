class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        arr=[]
        res=[]
        nums.sort()
        visited=set()

        def f(idx):
            if idx==n:
                if tuple(arr[:]) not in visited:
                    res.append(arr[:])
                    visited.add(tuple(arr[:]))
                return 
            arr.append(nums[idx])
            f(idx+1)
            arr.pop()
            f(idx+1)
        f(0)
        return res