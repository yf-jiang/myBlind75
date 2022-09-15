def pacificAtlantic(heights):
    n_rows, n_columns = len(heights), len(heights[0])
    pac, atl = set(), set()

    def dfs(r, c, ocean, prevHeight):
        if (r < 0 or r >= n_rows or c < 0 or c >= n_columns or
                (r, c) in ocean or heights[r][c] < prevHeight):
            return

        ocean.add((r, c))
        dfs(r + 1, c, ocean, heights[r][c])
        dfs(r - 1, c, ocean, heights[r][c])
        dfs(r, c + 1, ocean, heights[r][c])
        dfs(r, c - 1, ocean, heights[r][c])

    for col in range(n_columns):
        dfs(0, col, pac, heights[0][col])
        dfs(n_rows - 1, col, atl, heights[n_rows - 1][col])

    for row in range(n_rows):
        dfs(row, 0, pac, heights[row][0])
        dfs(row, n_columns - 1, atl, heights[row][n_columns - 1])

    # print(pac)
    # print(atl)

    res = []
    for r in range(n_rows):
        for c in range(n_columns):
            if (r, c) in pac and (r, c) in atl:
                res.append([r, c])

    return res


heights1 = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]
print(pacificAtlantic(heights1))
heights2 = [[1]]
print(pacificAtlantic(heights2))
