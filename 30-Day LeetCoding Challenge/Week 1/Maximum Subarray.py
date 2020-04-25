# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

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