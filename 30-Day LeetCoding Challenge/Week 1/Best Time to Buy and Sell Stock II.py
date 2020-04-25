#https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3287/

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