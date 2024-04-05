class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        return str_x == str_x[::-1]
        solution = Solution()
        number = int(input("Enter a number: "))
        print(solution.isPalindrome(number))
