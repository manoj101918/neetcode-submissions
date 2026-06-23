class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        c=0
        for i in range(len(nums)):
            if nums.count(nums[i])>1:
                c+=1

        if c>1:
            return True

        else:
            return False

        