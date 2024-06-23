class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        p1 = 0
        p2 = n - 1
        max_area = 0

        while p1 < p2:
            area = min(height[p1], height[p2]) * (p2 - p1)
            max_area = max(max_area, area)

            if height[p1] <= height[p2]:
                p1 += 1
            else:
                p2 -= 1

        return max_area
