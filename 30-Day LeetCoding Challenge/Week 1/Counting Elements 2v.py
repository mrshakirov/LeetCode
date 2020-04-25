#https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3289/

from typing import List
import collections

class LeetCode:
    def countElements(self, arr: List[int]) -> int:
        result = 0
        dict = {}
        
        for i in arr:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1

        for item in dict:
            if item + 1 in dict:
                if dict[item] > dict[item + 1]:
                    result += dict[item]
                else:
                    result += min(dict[item + 1], dict[item])
        return result

l = LeetCode()
print(l.countElements([1,1,2]))

# Complexity O(N^2) + N = O(N^2)