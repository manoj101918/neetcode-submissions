class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]
        nums=[]
        def f(start):
            if len(nums)==k:
                res.append(nums[:])
                return
            for i in range(start,n+1):
                nums.append(i)
                f(i+1)
                nums.pop()
        f(1)
        return res
        # arr=[i for i in range(1,n+1)]
        # res=[]
        # nums=[]
        # ln=len(arr)
        # def f(idx):
        #     if len(nums)==k:
        #         res.append(nums[:])
        #         return
        #     if len(nums)>k:
        #         return
        #     if idx==ln:
        #         return
        #     nums.append(arr[idx])
        #     f(idx+1)
        #     nums.pop()
        #     f(idx+1)

        # f(0)
        # return res

        