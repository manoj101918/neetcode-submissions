class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        arr = []
        res = []
        visited = set()
        dup1 = set()

        def f():
            if len(arr) == n:
                if tuple(arr) not in dup1:
                    res.append(arr[:])
                    dup1.add(tuple(arr))
                return

            for i in range(n):
                if i not in visited:
                    arr.append(nums[i])
                    visited.add(i)

                    f()

                    arr.pop()
                    visited.remove(i)

        f()
        return res