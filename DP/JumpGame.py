# Greedy
def canJump(nums):
    cur_goal = len(nums) - 1

    for i in range(len(nums) - 2, -1, -1):
        if i + nums[i] >= cur_goal:
            cur_goal = i

    if cur_goal == 0:
        return True
    else:
        return False


# DP
def dpCanJump(nums):
    cache = []

    def dfs(i):
        if i in cache:
            return False

        if i == len(nums) - 1:
            return True

        elif nums[i] == 0:
            cache.append(i)
            return False

        for j in range(1, nums[i] + 1):
            if dfs(i + j):
                return True

        return False

    return dfs(0)


# Brute Force DFS
def dfsCanJump(nums):
    n = len(nums)

    def dfs(i):
        if i == n - 1:
            return True

        if nums[i] == 0:
            return False

        for j in range(1, nums[i] + 1):
            if dfs(i + j):
                return True
        return False

    return dfs(0)


nums1 = [2, 3, 1, 1, 4]
nums2 = [3, 2, 1, 0, 4]
error1 = [0]
error2 = [1]
error3 = [2, 0, 0]
error4 = [2, 5, 0, 0]
error5 = [1, 2, 0, 1]
error6 = [2, 0, 2, 0, 1]
error7 = [3, 0, 8, 2, 0, 0, 1]
error8 = [0, 2, 3]
# print(canJump(nums1))
# print(canJump(nums2))
# print(canJump(error1))
# print(canJump(error2))
# print(canJump(error3))
# print(canJump(error4))
# print(canJump(error5))
# print(canJump(error6))
# print(canJump(error7))
print(canJump(error8))
