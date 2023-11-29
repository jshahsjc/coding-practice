"""
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

Example 1:
Input: grid = [
[0,0,1,0,0,0,0,1,0,0,0,0,0],
[0,0,0,0,0,0,0,1,1,1,0,0,0],
[0,1,1,0,1,0,0,0,0,0,0,0,0],
[0,1,0,0,1,1,0,0,1,0,1,0,0],
[0,1,0,0,1,1,0,0,1,1,1,0,0],
[0,0,0,0,0,0,0,0,0,0,1,0,0],
[0,0,0,0,0,0,0,1,1,1,0,0,0],
[0,0,0,0,0,0,0,1,1,0,0,0,0]
]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.

Example 2:
Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 50
grid[i][j] is either 0 or 1.

"""

def maxAreaIsland(grid):
    R = len(grid)
    C = len(grid[0])
    maxArea = 0
    def dfs(r,c):
        thisArea = 0
        if grid[r][c] == 1:
            thisArea += 1
            grid[r][c] = 0
        if r + 1 < R:
            thisArea += dfs(r + 1, c)
        if c + 1 < C:
            thisArea += dfs(r, c + 1)
        return thisArea
    for r in range(R):
        for c in range(C):
            if grid[r][c] == 1:
                maxArea = max(maxArea, dfs(r,c))
    return maxArea


def maxAreaIsland(grid):
    R = len(grid)
    C = len(grid[0])
    maxArea = 0
    def dfs(r,c):
        thisArea = 0
        if grid[r][c] == 1:
            thisArea += 1
            grid[r][c] = 0
        if r - 1 >= 0:
            thisArea += dfs(r - 1, c)
        if r + 1 < R:
            thisArea += dfs(r + 1, c)
        if c - 1 >= 0:
            thisArea += dfs(r, c - 1)
        if c + 1 < C:
            thisArea += dfs(r, c + 1)
        return thisArea
    for r in range(R):
        for c in range(C):
            if grid[r][c] == 1:
                maxArea = max(maxArea, dfs(r,c))
    return maxArea
