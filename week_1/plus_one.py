"""
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
"""


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        # add one to the last index digit of the array
        digits[-1] += 1
        # loop through each element in thee array getting their index
        for i in range(len(digits)):
            # if the given digit is eequal to 10
            if digits[-i - 1] == 10:
                # turn it into 0
                digits[-i - 1] = 0

                try:
                    # this is going backwards
                    digits[-i - 2] += 1
                except:
                    digits = [1] + digits
        return digits


# test case: [9,9,9,9] + 1 answer --> [1,0,0,0,0]
