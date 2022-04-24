# https://leetcode.com/problems/number-of-islands/
# might not work in leetcode after copy and pasting.

def numIslands(grid: list[list[str]]) -> int:
    island_count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                island_count += dfs_num_of_islands(i, j, grid)
    return island_count


def dfs_num_of_islands(i: int, j: int, grid: list[list[str]]) -> int:
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':
        return 0
    grid[i][j] = '0'
    dfs_num_of_islands(i + 1, j, grid)
    dfs_num_of_islands(i - 1, j, grid)
    dfs_num_of_islands(i, j + 1, grid)
    dfs_num_of_islands(i, j - 1, grid)
    return 1
