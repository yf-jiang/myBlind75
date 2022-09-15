class Solution:
    @staticmethod
    def maxProfit(prices):
        #         n = len(prices)
        #         max_profit = float('-inf')

        #         for i in range(n):
        #             for j in range(i, n):
        #                 curr_profit = prices[j] - prices[i]
        #                 if curr_profit >= max_profit:
        #                     max_profit = curr_profit

        #         if max_profit <= 0:
        #             return 0

        #         else:
        #             return max_profit

        min_price = float('inf')
        max_profit = 0

        for p in prices:
            if p < min_price:
                min_price = p
            elif (p - min_price) > max_profit:
                max_profit = p - min_price

        return max_profit


solver = Solution
case1 = [7, 1, 5, 3, 6, 4]
print(solver.maxProfit(case1))

