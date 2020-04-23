#Given an integer array arr, count element x such that x + 1 is also in arr.

#If there're duplicates in arr, count them seperately.

from typing import List
import collections

class LeetCode:
    def countElements(self, arr: List[int]) -> int:
        result = 0
        dict = {}
        
        for i in arr:
            dict[i] = 1

        for item in dict:
            if item + 1 in dict:
                result += 1
        return result

l = LeetCode()
print(l.countElements([1,1,2]))

# Complexity O(N)