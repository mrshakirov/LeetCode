#https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/529/week-2/3298/

from typing import List
from collections import defaultdict

class LeetCode:
    def findMaxLength(self, nums: List[int]) -> int:
        count = defaultdict(list)
        count[0] = [-1]
        sum = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                sum -= 1
            else:
                sum += 1
            count[sum].append(i)
        
        ans = 0
        for key, value in count.items():
            if len(value) > 1:
                ans = max(ans, value[-1] - value[0])
        return ans

l = LeetCode()
print(l.findMaxLength([0,1]))

# Complexity is O(N)