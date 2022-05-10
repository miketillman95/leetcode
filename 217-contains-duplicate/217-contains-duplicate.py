class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numSet = (set(nums))
        # print(len(numSet))
        # print(len(nums))
        
        return not  len(numSet) == len(nums)