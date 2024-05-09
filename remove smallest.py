def check_array():
    n=int(input())
    nums = list(map(int, input().split()))
    nums.sort()

    for i in range(len(nums) - 1):
        if nums[i+1] - nums[i]> 1:
            return "NO"
        else:
            pass

    return "YES"

t = int(input())
for _ in range(t):
    print(check_array())
