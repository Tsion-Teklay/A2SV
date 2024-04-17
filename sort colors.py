class Solution(object):
    def sortColors(self, nums):
        counter=[0]*3

        for num in nums:
            counter[num]+=1

        i=0
        for color in range(3):
            for item in range(counter[color]):
                nums[i]=color
                i+=1
        return nums       
        
