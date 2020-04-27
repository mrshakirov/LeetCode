#https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/529/week-2/3292/

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = []
        
        
    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.min: 
            self.min.append(x)
        else:
            self.min.append(min(self.min[-1], x)) 
        
        
    def pop(self) -> None:
        self.min.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()