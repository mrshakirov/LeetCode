#https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/529/week-2/3291/

from typing import List

class LeetCode:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def process(S):
            ans = []
            for c in S:
                if c != '#':
                    ans.append(c)
                elif ans:
                    ans.pop()
            return "".join(ans)
        return process(S) == process(T)

l = LeetCode()
print(l.backspaceCompare("oi###mupo##rszty#s#xu###bxx##dqc#gdjz","oi###mu#ueo##pk#o##rsztu#y#s#xu###bxx##dqc#gz#djz"))

# Complexity O(M+N), where M and N lenght of S and T respectively