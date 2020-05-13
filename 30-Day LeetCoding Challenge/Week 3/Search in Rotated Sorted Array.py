#https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/530/week-3/3304/

from typing import List

class LeetCode:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > nums[start]:
                if nums[start] <= target and nums[mid] > target:
                    end = mid
                else:
                    start = mid
            else:
                if nums[mid] < target and nums[end] >= target:
                    start = mid
                else:
                    end = mid

        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1
        
l = LeetCode()
print(l.search([4,5,6,7,0,1,2], 3))

#Complexity O(logN), where N numbers of elements in array