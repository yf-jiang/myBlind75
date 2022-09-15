def search(nums, target):
    return binarySearch(nums, target, 0, len(nums)-1)


# def binarySearch(nums, target, start, end):
#     # print(start, end)
#     if start > end:
#         return -1
#     mid = (start+end)//2
#     if nums[mid] == target:
#         return mid
#     # check if start..mid array is sorted
#     if nums[start] <= nums[mid]:
#         if nums[mid] > target >= nums[start]:
#             # recurse in left array
#             return binarySearch(nums, target, start, mid-1)
#         else:
#             # recurse in right array
#             return binarySearch(nums, target, mid+1, end)
#     else:
#         if nums[mid] < target <= nums[end]:
#             # recurse to right array
#             return binarySearch(nums, target, mid+1, end)
#         else:
#             # recurse to left array
#             return binarySearch(nums, target, start, mid-1)


def binarySearch(arr, x, l, r):

    if r >= l:
        mid = l + (r - l) // 2

        if arr[mid] == x:
            return mid

        if arr[l] <= arr[mid]:
            if arr[mid] > x >= arr[l]:
                return binarySearch(arr, x, l, mid - 1)
            else:
                return binarySearch(arr, x, mid + 1, r)

        else:
            if arr[mid] < x <= arr[r]:
                return binarySearch(arr, x, mid+1, r)
            else:
                return binarySearch(arr, x, l, mid-1)

    else:
        return -1


nums1 = [4, 5, 6, 7, 0, 1, 2]
target1 = 0
print(search(nums1, target1))
nums2 = [4, 5, 6, 7, 0, 1, 2]
target2 = 3
print(search(nums2, target2))
nums3 = [1]
target3 = 0
print(search(nums3, target3))
