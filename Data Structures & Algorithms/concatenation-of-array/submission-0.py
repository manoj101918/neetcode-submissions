class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        temp=nums
        for i in range(len(nums)):
            temp.append(nums[i])


        return temp

        
        