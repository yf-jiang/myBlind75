class Solution:
    @staticmethod
    def maxProduct(nums):
        mx = 1
        mn = 1
        ans = float("-inf")

        for num in nums:
            mx, mn = max(num, mx * num, mn * num), min(num, mx * num, mn * num)
            ans = max(mx, mn, ans)

        return ans

    # @staticmethod
    # def dpSolution(nums):


example1 = [2, 3, -2, 4]
print(Solution.maxProduct(example1))
error1 = [-2, 3, -4]
print(Solution.maxProduct(error1))
