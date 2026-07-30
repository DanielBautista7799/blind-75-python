"""Solution for LeetCode 121: Best Time to Buy and Sell Stock."""


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        currentlow = prices[0]

        for price in prices:
            currentlow = min(currentlow, price)
            profit = max(price - currentlow, profit)

        return profit
