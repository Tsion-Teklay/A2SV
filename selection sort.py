class Solution:
    def select(self, arr, i):
        n = len(arr)
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        return min_idx

    def selectionSort(self, arr,n):
        n = len(arr)
        for i in range(n-1):
            mini = self.select(arr, i)
            arr[i], arr[mini] = arr[mini], arr[i]
