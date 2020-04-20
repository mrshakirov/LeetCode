# Write an algorithm to determine if a number n is "happy".

# A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

# Return True if n is a happy number, and False if not.

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