def rob(nums):
    if len(nums) == 1:
        return nums[0]

    dpArr = [nums[0], nums[1]] + [0] * (len(nums) - 2)
    cur_max = max(nums[0], nums[1])

    for i in range(2, len(dpArr)):
        tempArr = dpArr[:i-1]
        dpArr[i] = max(tempArr) + nums[i]

        if dpArr[i] > cur_max:
            cur_max = dpArr[i]

        # for j in range(0, i):
        #     if j != i - 1:
        #         cur = dpArr[j] + nums[i]
        #         if cur > dpArr[i]:
        #             dpArr[i] = cur
        #
        #         if dpArr[i] > cur_max:
        #             cur_max = dpArr[i]

    return cur_max


nums1 = [1, 2, 3, 1]
nums2 = [2, 7, 9, 3, 1]
edge1 = [2, 2]
edge2 = [1]
error1 = [2, 1, 1, 2]
print(rob(nums1))
print(rob(nums2))
print(rob(edge1))
print(rob(edge2))
print(rob(error1))
