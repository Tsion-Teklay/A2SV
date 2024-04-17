class Solution(object):
    def targetIndices(self, nums, target):
        n=len(nums)
        output=[]
        nums2=sorted(nums)
        for i in range(n):
            if nums2[i] == target:
                output.append(i)
        return output    
