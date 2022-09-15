def twoSum(nums, target):
    dick = {}

    for i in range(len(nums)):
        diff = target - nums[i]

        if nums[i] in dick:
            # print('dick', dick)
            # print(nums[i])
            return [dick[nums[i]], i]

        else:
            dick[diff] = i
            # print(dick)

    # ind_list = []
    # length = len(nums)
    #
    # for i in range(length):
    #     for j in range(length):
    #         if (nums[i] + nums[j]) == target:
    #             if i not in ind_list and j not in ind_list and i != j:
    #                 ind_list.append(i)
    #                 ind_list.append(j)
    #
    # return ind_list


def another(nums, target):
    nums.sort()
    ans = []
    l = 0
    r = len(nums) - 1

    while l < r:

        diff = target - (nums[l] + nums[r])
        # print(diff)

        if diff > 0:
            l += 1
        elif diff < 0:
            r -= 1
        else:
            return [nums[l], nums[r]]

            # while nums[l] == nums[l - 1] and l < r:
            #     l += 1

    return ans


# nums = [2, 7, 11, 15]
nums = [11, 15, 2, 7]

err1 = [3, 2, 4]
target = 6
print(another(err1, target))
