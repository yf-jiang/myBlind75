def lengthOfLIS(nums):
    dpArr = [0] * (len(nums) - 1) + [1]

    for i in range(len(nums)-1, -1, -1):
        tempArr = [1]

        for j in range(i+1, len(nums)):

            if nums[j] > nums[i]:
                tempArr.append(1 + dpArr[j])
                # dpArr[i] = max(dpArr[i], 1 + dpArr[j])

        dpArr[i] = max(tempArr)
    print(dpArr)
    return max(dpArr)


ex = [1, 2, 4, 3]
nums0 = [0, 3, 1, 6, 2, 2, 7]
nums1 = [10, 9, 2, 5, 3, 7, 101, 18]
nums2 = [0, 1, 0, 3, 2, 3]
nums3 = [7, 7, 7, 7, 7, 7, 7]

print(lengthOfLIS(ex))
print(lengthOfLIS(nums0))
print(lengthOfLIS(nums1))
print(lengthOfLIS(nums2))
print(lengthOfLIS(nums3))
