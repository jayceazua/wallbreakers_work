"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""


class Solution:
    def reverse(self, x: int) -> int:
        # check if the input is a negative number
        is_negative = False
        if x < 0:
            is_negative = True
            x = abs(x)

        reversed_num = 0 # 3

        while x != 0:
            reversed_num = (reversed_num * 10) + (x % 10) # 
            x = x // 10

        # corner/ edge cases
        if is_negative:
            if (reversed_num * -1) < ((2**31) * -1):
                return 0
            return reversed_num * -1
        elif reversed_num == 0 or reversed_num > (2**31 - 1):
            return 0

        return reversed_num
