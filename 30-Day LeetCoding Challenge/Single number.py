#Given a non-empty array of integers, every element appears twice except for one. Find that single one.

#Note:

#Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

from typing import List

class LeetCode:
    def singleNumber(self, nums: List[int]) -> int:
            nums.sort()
            length = len(nums)
            pair_first_idx = 0
            pair_second_idx = 1
            while (pair_first_idx < length and pair_second_idx < length):
                if nums[pair_first_idx] != nums[pair_second_idx]:
                    break
                pair_first_idx += 2
                pair_second_idx += 2
            return nums[pair_first_idx]

l = LeetCode()
print(l.singleNumber([4,1,2,1,2]))

# Complexity O(n log n) + n = O(n log n)