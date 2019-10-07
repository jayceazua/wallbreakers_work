"""
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 

Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
"""


class Solution:
    def __init__(self):
        self.solved = set()

    def isHappy(self, n: int) -> bool:
        """
        Starting with any positive integer, 
            replace the number by the sum of the squares of its digits, 
                and repeat the process until the number equals 1 (where it will stay), 
                    or it loops endlessly in a cycle which does not include 1. 

        Those numbers for which this process ends in 1 are happy numbers.
        """
        if n == 1:
            return True

        num = 0

        while n >= 1:

            q, r = divmod(n, 10)

            n = q

            num += r**2

        # adds to the cycle, if the num total has already been solved then we know it will run into a cycle
        if num in self.solved:
            return False

        self.solved.add(num)

        return self.isHappy(num)
