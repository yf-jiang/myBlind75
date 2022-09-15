import copy


class Solution:
    @staticmethod
    def productExceptSelf(nums):
        n = len(nums)
        forwards = []
        backwards = []
        reverse_nums = copy.deepcopy(nums)
        reverse_nums.reverse()
        forward_product = 1
        backward_product = 1

        for num in nums:
            forward_product *= num
            forwards.append(forward_product)

        for num in reverse_nums:
            backward_product *= num
            backwards.append(backward_product)

        ans = [backwards[n - 2]]

        for i in range(1, n - 1):
            curr = forwards[i - 1] * backwards[n - i - 2]
            ans.append(curr)

        ans.append(forwards[n - 2])

        return ans


nums = [1, 2, 3, 4]
print(Solution.productExceptSelf(nums))
nums = [-1, 1, 0, -3, 3]
print(Solution.productExceptSelf(nums))
