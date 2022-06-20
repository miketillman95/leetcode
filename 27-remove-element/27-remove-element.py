class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        print(val)
        while val in nums: nums.remove(val)