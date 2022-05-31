class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if (len(nums) ==0):
            return 0
        
        nums.sort()
        for n in range(len(nums)):
            print(range(len(nums)))
            
            if n!=nums[n]:
                return n
            
        return len(nums)
            