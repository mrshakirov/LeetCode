#https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3288/

from typing import List
import collections

class LeetCode:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()
l = LeetCode()
print(l.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

# Complexity O(NKlogK), where N is lenght of list, K is the maximum lenght of sting in list