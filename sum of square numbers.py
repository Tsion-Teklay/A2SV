class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left=0
        right=int(c**0.5)

        while left<=right:
            if left*left + right * right==c:
                return True
            elif left*left + right * right < c:
                left+=1
            else:
                right-=1
        
        return False
