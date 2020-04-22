#Say you have an array prices for which the ith element is the price of a given stock on day i.

#Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

#Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

from typing import List

class LeetCode:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for index in range(len(prices[1:])):
            index = index + 1
            if prices[index] > prices[index - 1]:
                profit += prices[index] - prices[index - 1]
        return profit
l = LeetCode()
print(l.maxProfit([7,1,5,3,6,4]))

# Complexity O(n)