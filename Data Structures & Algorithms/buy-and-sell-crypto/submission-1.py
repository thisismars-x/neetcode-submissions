class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        max_profit = 0

        end = 0

        selling = buying = prices[0]
        while end < n:
            if prices[end] > buying:
                buying = prices[end]
                max_profit = max(max_profit, buying - selling)
            elif prices[end] < selling:
                buying = selling = prices[end]

            end += 1

        return max_profit
