class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        i = 1
        while i > 0:
            if (i * n) % 2 == 0:
                return (i * n)
                break
            else:
                i += 1
