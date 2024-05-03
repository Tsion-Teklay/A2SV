class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        m=len(nums1)
        n=len(nums2)
        p1=0
        p2=0

        while p1<m and p2<n:
            if nums1[p1]<nums2[p2]:
                p1+=1
            elif nums2[p2]<nums1[p1]:
                p2+=1
            else:
                return nums1[p1]

        return -1
