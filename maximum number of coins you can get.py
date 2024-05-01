class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()  
        n = len(piles)
        max_sum = 0
        i = n - 2  # Start from the second largest pile

        while i >= n // 3:
            max_sum += piles[i]
            i -= 2  # Skip two piles at a time

        return max_sum
