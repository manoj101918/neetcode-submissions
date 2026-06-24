class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        arr=[]
        res=[]
        visited=set()
        def f():
            if len(nums)==len(arr):
                res.append(arr[:])
                return
            for num in nums:
                if num not in visited:
                    arr.append(num)
                    visited.add(num)
                    f()
                    arr.pop()
                    visited.remove(num)
        f()
        return res
        