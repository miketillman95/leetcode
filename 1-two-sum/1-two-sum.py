class Solution(object):
    def twoSum(self, nums, target):
        
        goal = {}
        
        for i in range(len(nums)):
            # print(range(len(nums)))
            if nums[i] in goal:
                # print(i)
                return [ i, goal[nums[i]]]
            # print(nums[i])   
            goal[target- nums[i]] = i
        