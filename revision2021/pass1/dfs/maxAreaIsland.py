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

def getMaxAreaIsland(grid):
    seen = set()
    max_area = 0
    def dfs_area(r, c):
        area = 0
        if (0 <= r < len(grid)) \
            and (0 <= c < len(grid[0])) \
            and ((r,c) not in seen) \
            and (r, c) == 1:
            seen.add((r,c))
            area = 1 + dfs_area(r + 1, c) + dfs_area(r - 1, c)
                     + dfs_area(r, c + 1) + dfs_area(r, c - 1)
        return area

    for r in grid:
        for c in r:
            if dfs_area((r, c)) > max_area:
                max_area = dfs_area((r, c))

    return max_area





def maxAreaIsland(grid):
    rows = len(grid)
    cols = len(grid[0])
    max_area = 0
    def dfs(r, c):
        my_area = 0
        if grid[r][c] == 1:
            my_area += 1
            grid[r][c] = 0
            if r - 1 >= 0:
                my_area += dfs(r - 1, c)
            if c - 1 >= 0:
                my_area += dfs(r, c - 1)
            if r + 1 < rows:
                my_area += dfs(r + 1, c)
            if c + 1 < cols:
                my_area += dfs(r, c + 1)
        return my_area
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                max_area = max(max_area, dfs(r, c))
    return max_area
