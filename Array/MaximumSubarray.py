class Solution:
    @staticmethod
    def bruteForce(nums):
        maximum = float('-inf')
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                # print(i, j, nums[i:j + 1])
                partition_sum = sum(nums[i:j + 1])
                # print(partition_sum)
                if partition_sum > maximum:
                    maximum = partition_sum

        return maximum

    @staticmethod
    # DP implementation
    def maxSubArray(nums):
        n = len(nums)
        curr = nums[0]
        maximum = nums[0]

        for i in range(1, n):
            # This line needs some thought
            curr = max(nums[i], curr + nums[i])
            maximum = max(maximum, curr)

        return maximum


example1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(Solution.maxSubArray(example1))
example2 = [1]
print(Solution.maxSubArray(example2))
example3 = [5, 4, -1, 7, 8]
print(Solution.maxSubArray(example3))
error1 = [-2, -1]
print(Solution.maxSubArray(error1))
