class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res1=0
        n=len(nums)
        def f(idx):
            nonlocal res1
            if idx==n:
                res=0
                for i in range(len(arr)):
                    res^=arr[i]
                res1+=res
                return 
            arr.append(nums[idx])
            f(idx+1)
            arr.pop()
            f(idx+1)
        arr=[]
        f(0)
        return res1

        