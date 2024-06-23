class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        n=len(nums)
        nums.sort()
        p1=0
        p2=n-1
        counter=0

        while p1<p2:
            if nums[p1]+nums[p2]==k:
                counter+=1
                p1+=1
                p2-=1
            elif nums[p1]+nums[p2]>k:
                p2-=1
            else:
                p1+=1
        
        return counter
