class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)
        lprod = 1
        rprod = 1
        
        for i in range(len(nums)):
            res[i] *= lprod
            lprod *= nums[i]
            
            res[~i] *= rprod
            print('rprod', rprod)
            rprod *= nums[~i]
            print('nums', nums[~i])
            
        return res
            
 
        