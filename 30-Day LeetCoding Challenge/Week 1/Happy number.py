#https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3284/

from typing import List

class LeetCode:
    
    
    def isHappy(self, n: int) -> bool:
        number_of_iterations = 1000
        temp_number = n
        while number_of_iterations != 0:
            temp_number = self.CalcHappy(temp_number)
            if temp_number == 1:
                return True
            number_of_iterations -= 1
        return False

    def CalcHappy(self, n: int) -> bool:
        num = str(n)
        sum = 0
        for n in range(len(num)):
            sum += int(num[n]) * int(num[n])
        return sum

l = LeetCode()
print(l.isHappy(19))

# Complexity m - number of iterations to check if number is Happry or not