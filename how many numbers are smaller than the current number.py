class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        n=len(nums)
        result=[]
        for i in range(n):
            counter=0
            for j in range(n):
                if nums[j]<nums[i]:
                    counter+=1
            result.append(counter)
        return result

                
                 

        
