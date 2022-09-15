def rob(nums):
    return max(nums[0], rob1(nums[:-1]), rob1(nums[1:]))


def rob1(nums):
    if len(nums) == 1:
        return nums[0]

    dpArr = [nums[0], nums[1]] + [0] * (len(nums) - 2)
    cur_max = max(nums[0], nums[1])

    for i in range(2, len(dpArr)):
        tempArr = dpArr[:i-1]
        dpArr[i] = max(tempArr) + nums[i]

        if dpArr[i] > cur_max:
            cur_max = dpArr[i]

    return cur_max


nums1 = [2, 3, 2]
nums2 = [1, 2, 3, 1]
nums3 = [1, 2, 3]
error1 = [1, 2, 1, 1]
error2 = [200, 3, 140, 20, 10]
error3 = [1, 2, 1, 0]
error4 = [0]
# print(rob(nums1))
# print(rob(nums2))
# print(rob(nums3))
# print(rob(error1))
# print(rob(error2))
# print(rob(error3))
print(rob(error4))
