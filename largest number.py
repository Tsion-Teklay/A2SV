class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))
        largest = sorted(nums, key=lambda x: x*9, reverse=True)
        result = ''.join(largest)

        # Handle the case where the result is '0'
        return result if result[0] != '0' else '0'
