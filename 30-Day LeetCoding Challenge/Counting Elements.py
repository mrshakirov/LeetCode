#Given an integer array arr, count element x such that x + 1 is also in arr.

#If there're duplicates in arr, count them seperately.

from typing import List
import collections

class LeetCode:
    def countElements(self, arr: List[int]) -> int:
        result = 0
        arr.sort()
        g = {}
        for i in arr:
            if i in g: 
                g[i] += 1
            else: 
                g[i] = 1
        keys = list(g.keys())
        for idx in range(len(keys[1:])):
            idx += 1
            if keys[idx] - keys[idx - 1] == 1:
                if g[keys[idx - 1]] > g[keys[idx]]:
                    result += g[keys[idx - 1]]
                else:
                    result += min(g[keys[idx - 1]], g[keys[idx]])
        return result
l = LeetCode()
print(l.countElements([1,1,2]))

# Complexity Nlog(N) sorting + N^2 + K (unique enties)