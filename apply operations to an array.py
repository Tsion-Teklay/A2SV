class Solution(object):
    def applyOperations(self, nums):
        n = len(nums)
        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        
        left = 0
        for i in range(n):
            if nums[i] != 0:
                nums[left] = nums[i]
                left += 1
        
        for i in range(left, n):
            nums[i] = 0
        
        return nums
