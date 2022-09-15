def longestConsecutive(nums):
    hashset = set(nums)
    longestLength = 0

    for num in nums:
        if num - 1 not in hashset:
            length = 0
            i = 0

            while num + i in hashset:
                length += 1
                i += 1
            longestLength = max(longestLength, length)

    return longestLength


nums1 = [100, 4, 200, 1, 3, 2]
nums2 = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
print(longestConsecutive(nums1))
print(longestConsecutive(nums2))
