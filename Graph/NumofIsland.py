def numIslands(grid):
    if not grid:
        return 0

    n_rows, n_columns = len(grid), len(grid[0])
    count = 0
    visited = set()

    def detectIsland(row, col):
        if row < 0 or col < 0 or row == n_rows or col == n_columns:
            return

        if grid[row][col] == "1" and (row, col) not in visited:
            visited.add((row, col))

            detectIsland(row + 1, col)
            detectIsland(row - 1, col)
            detectIsland(row, col + 1)
            detectIsland(row, col - 1)
        # return

    for i in range(n_rows):
        for j in range(n_columns):
            if grid[i][j] == "1" and (i, j) not in visited:
                detectIsland(i, j)
                count += 1

    return count


grid1 = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]

grid2 = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]

print(numIslands(grid1))
print(numIslands(grid2))
