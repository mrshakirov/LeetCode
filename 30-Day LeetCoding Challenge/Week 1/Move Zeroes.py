#https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3286/

from typing import List

class LeetCode:
    def moveZeroes(self, nums: List[int]) -> None:
            idx = 0
            for i in range(len(nums)):
                if nums[i] != 0:
                    nums[idx] = nums[i]
                    idx += 1
            while idx < len(nums):
                nums[idx] = 0
                idx += 1
            return nums

l = LeetCode()
print(l.moveZeroes([0,1,0,3,12]))

# Complexity O(n^2)