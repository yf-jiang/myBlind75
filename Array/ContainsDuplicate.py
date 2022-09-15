class Solution:
    @staticmethod
    def containsDuplicate(nums) -> bool:
        #         visited = []

        #         for number in nums:
        #             if number in visited:
        #                 return True
        #             else:
        #                 visited.append(number)

        #         return False

        memo = set()
        for val in nums:
            if val in memo:
                return True
            else:
                memo.add(val)

        return False

    @staticmethod
    def o1space_solution(nums):
        nums.sort()

        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True

        return False

    @staticmethod
    def simple(nums):
        visited = set()

        for num in nums:
            visited.add(num)

        return not len(visited) == len(nums)

solver = Solution
case1 = [1, 2, 3, 1]
error_case = [1, 2, 3, 4]
print(solver.simple(case1))
print(solver.o1space_solution(error_case))

