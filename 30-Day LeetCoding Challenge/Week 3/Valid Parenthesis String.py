#https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/530/week-3/3301/

from typing import List

class LeetCode:
    def checkValidString(self, s: str) -> bool:
        max_l = 0
        max_r = 0
        for i in range(len(s)):
        
            # left side
            if s[i] != ')':
                max_l += 1
            else:
                max_l -= 1
            
            if max_l < 0: return False

            # right side
            if s[-i - 1] != '(':
                max_r += 1
            else:
                max_r -= 1
            if max_r < 0: return False

        return True

l = LeetCode()
print(l.checkValidString("(*))"))

#Complexity O(N), N - numbers of integers in array