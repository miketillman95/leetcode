class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        for n in range(len(nums)):
            print(range(len(nums)))
            nums.sort()
            print(nums.sort())
            if n!=nums[n]:
                return n
        return len(nums)
            