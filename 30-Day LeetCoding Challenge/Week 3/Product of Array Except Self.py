#https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/530/week-3/3300/

from typing import List

class LeetCode:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        prod_left = [1] * size
        prod_right = [1] * size
        result = []

        for i in range(size - 1):
            prod_left[i + 1] *= prod_left[i] * nums[i]

        for i in range(size - 1, 0, -1):
            prod_right[i - 1] *= prod_right[i] * nums[i]
        
        for i in range(size):
            result.append(prod_left[i] * prod_right[i])
        return result


l = LeetCode()
print(l.productExceptSelf([0,1]))

#Complexity O(N), N - numbers of integers in array