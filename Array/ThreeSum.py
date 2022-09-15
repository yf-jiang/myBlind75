import copy
from itertools import permutations


def threeSum(nums):
    nums.sort()
    ans = []

    for i, a in enumerate(nums):
        if i > 0 and a == nums[i - 1]:
            continue

        l = i + 1
        r = len(nums) - 1

        while l < r:
            threesome = a + nums[l] + nums[r]

            if threesome > 0:
                r -= 1
            elif threesome < 0:
                l += 1
            else:
                ans.append([a, nums[l], nums[r]])
                l += 1

                while nums[l] == nums[l - 1] and l < r:
                    l += 1

    return ans


# def twoSum(nums, target):
#     dick = {}
#
#     for i in range(len(nums)):
#         diff = target - nums[i]
#
#         if nums[i] in dick:
#             # print('dick', dick)
#             # print(nums[i])
#             return [dick[nums[i]], i]
#
#         else:
#             dick[diff] = i
#
#     return False


# def reduceAns(l2):
#     ans = []
#     parr = []
#
#     for l in l2:
#         perm = permutations(l)
#         for p in perm:
#             temp = list(p)
#             if temp != l:
#                 parr.append(temp)
#
#     print(parr)
#
#     for l in l2:
#         if l not in parr:
#             ans.append(l)
#
#     return ans


nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums))
