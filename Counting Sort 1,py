import math
import os
import random
import re
import sys

def countingSort(arr):
    n = len(arr)
    #m = max(arr) + 1  # Add 1 to account for zero as a value
    arr2 = [0] * 100
    for i in range(n):
        arr2[arr[i]] += 1
    return arr2

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = countingSort(arr)
    print(' '.join(map(str, result)))
