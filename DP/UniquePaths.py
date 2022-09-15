def uniquePaths(m, n):
    dpMatrix = [[0 for j in range(n + 1)] for i in range(m + 1)]
    dpMatrix[m - 1][n] = 1

    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            # print(i, j)
            # print(dpMatrix[i][j + 1], dpMatrix[i + 1][j])
            dpMatrix[i][j] = dpMatrix[i][j + 1] + dpMatrix[i + 1][j]
            # print(dpMatrix)

    return dpMatrix[0][0]


m1 = 3
n1 = 7
m2 = 3
n2 = 2
print(uniquePaths(m1, n1))
print(uniquePaths(m2, n2))
