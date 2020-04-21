#Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

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