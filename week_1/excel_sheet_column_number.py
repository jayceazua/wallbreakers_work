"""
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...
Example 1:

Input: "A"
Output: 1
Example 2:

Input: "AB"
Output: 28
Example 3:

Input: "ZY"
Output: 701
"""


class Solution:
    def titleToNumber(self, s: str) -> int:
        letters = reversed(s)  # O(n) time/ space
        total_sum = 0  # O(1) space
        for index, letter in enumerate(letters):  # O(n) time
            total_sum += (ord(letter) - 64) * 26 ** index
        return total_sum

        # convert the letter

        # multiply it by 26
        # and bring it to the power of it's position
