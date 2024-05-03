class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n=len(nums)
        zp=0

        for i in range(n):
            if nums[i]!=0:
                nums[zp]=nums[i]
                zp+=1

        while zp<n:
            nums[zp]=0
            zp+=1
