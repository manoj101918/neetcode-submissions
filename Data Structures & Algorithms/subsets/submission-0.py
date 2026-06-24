class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        visited=set()
        n=len(nums)
        res=[]
        def f(idx,arr):
            if idx==n:
                x=arr[:]
                if tuple(x) not in visited:
                    res.append(x)
                    visited.add(tuple(x))
                return
            #pick
            arr.append(nums[idx])
            f(idx+1,arr)
            arr.pop()
            f(idx+1,arr)
        f(0,[])
        return res

        