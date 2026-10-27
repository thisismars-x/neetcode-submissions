class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        max_profit = 0

        start = end = 0

        selling = buying = prices[start]
        while end < n:
            if prices[end] > buying:
                buying = prices[end]
                max_profit = max(max_profit, buying - selling)
            elif prices[end] < selling:
                selling = prices[end]
                buying = selling

            end += 1

        return max_profit
