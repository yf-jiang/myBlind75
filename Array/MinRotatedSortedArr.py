def findMin(nums):
    n = len(nums)
    if n == 1:
        return nums[0]
    if n == 2:
        if nums[0] <= nums[1]:
            return nums[0]
        else:
            return nums[1]
    elif nums[0] < nums[n - 1]:
        return nums[0]

    mid = n // 2
    if nums[mid] > nums[mid + 1]:
        return nums[mid + 1]

    if nums[mid - 1] > nums[mid]:
        return nums[mid]

    elif nums[mid] > nums[0]:
        # search right
        return findMin(nums[mid + 1:])

    elif nums[mid] < nums[0]:
        # search left
        return findMin(nums[:mid])


# nums1 = [3, 4, 5, 1, 2]
# print(findMin(nums1))
# nums2 = [4, 5, 6, 7, 0, 1, 2]
# print(findMin(nums2))
# nums3 = [11, 13, 15, 17]
# print(findMin(nums3))
# error1 = [2, 1]
# print(findMin(error1))
error2 = [2, 3, 4, 5, 1]
print(findMin(error2))
