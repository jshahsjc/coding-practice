"""
An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and newColor. You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with newColor.

Return the modified image after performing the flood fill.

Example 1:

Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.
Example 2:

Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, newColor = 2
Output: [[2,2,2],[2,2,2]]


Constraints:

m == image.length
n == image[i].length
1 <= m, n <= 50
0 <= image[i][j], newColor < 216
0 <= sr < m
0 <= sc < n
"""

def fillColor(image, sr, sc, new_color):
    i = j = 0
    rows = len(image)
    cols = len(image[0])
    match_color = image[sr][sc]
    def dfs(r, c):
        if image[r, c] == match_color:
            image[r, c] = new_color
        if r - 1 >= 0:
            dfs(r -1, c)
        if r + 1 < R:
            dfs(r + 1, c)
        if c - 1 >= 0:
            dfs(r, c - 1)
        if c + 1 < cols:
            dfs(r, c + 1)
    dfs(sr, sc)
    return image





"""
An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and newColor. You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with newColor.

Return the modified image after performing the flood fill.

Example 1:

Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.
Example 2:

Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, newColor = 2
Output: [[2,2,2],[2,2,2]]


Constraints:

m == image.length
n == image[i].length
1 <= m, n <= 50
0 <= image[i][j], newColor < 216
0 <= sr < m
0 <= sc < n
"""


def floodFill(image, sr, sc, new_color):
    if image[sr][sc] == new_color:
        return image
    match_color = image[sr][sc]
    def dfs(r, c):
        if 0 <= r < len(image) and 0 <= c <len(image[0]) and image[r][c] == match_color:
            image[r][c] = new_color
            if r + 1 < len(image):
                dfs(r + 1, c)
            if r - 1 >= 0:
                dfs(r - 1, c)
            if c + 1 < len(image[0]):
                dfs(r, c + 1)
            if c - 1 >= 0:
                dfs(r, c - 1)
    dfs(sr, sc)
    return image
