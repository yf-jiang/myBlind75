def combinationSum(candidates, target):
    res = []

    def dfs(i, cur, total):
        if total == target:
            res.append(cur.copy())
            return

        if i >= len(candidates) or total > target:
            return

        cur.append(candidates[i])
        dfs(i, cur, total + candidates[i])
        cur.pop()
        dfs(i + 1, cur, total)

    dfs(0, [], 0)
    return res


candidates1 = [2, 3, 6, 7]
target1 = 7
candidates2 = [2, 3, 5]
target2 = 8
candidates3 = [2]
target3 = 1
print(combinationSum(candidates1, target1))
print(combinationSum(candidates2, target2))
print(combinationSum(candidates3, target3))
