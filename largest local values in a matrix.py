class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n=len(grid)
        max_local=[[0]*(n-2) for _ in range(n-2)]

        for i in range(n-2):
            for j in range(n-2):
                submatrix=[
                    [grid[i+r][j+c]for c in range(3)] for r in range(3)]
                max_local[i][j]=max(max(row)for row in submatrix)
        return max_local
        
