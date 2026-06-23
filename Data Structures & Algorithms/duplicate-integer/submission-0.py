class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n= len(nums)
        n1=len(set(nums))
        if n!=n1:
            return True
        else:
            return False        