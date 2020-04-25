#https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3285/

from typing import List

class LeetCode:
    
    def maxSubArray(self, nums: List[int]) -> int:
        temp_sum = 0
        result = nums[0]
        for item in nums:
            temp_sum += item
            if result < temp_sum:
                result = temp_sum
            if temp_sum < 0:
                temp_sum = 0
        return result

l = LeetCode()
print(l.maxSubArray([-1]))

# O(n)