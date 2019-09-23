"""
A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

Also, a self-dividing number is not allowed to contain the digit zero.

Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.

Example 1:
Input: 
left = 1, right = 22
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
"""


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        # for i in range(left, right + 1):
        #     valid = True
        #     if str(i).find("0") != -1:
        #         valid = False
        #     for j in str(i).split():
        #         if i % int(j) != 0:
        #             valid = False
        #     if valid:
        #         output.append(i)
        # return output

        # 128
        output = []

        for n in range(left, right + 1):
            if self.self_dividing(n):
                output.append(n)

        return output

    # help function to return True or False if the digit given is self_dividing

    def self_dividing(self, n):
        # make a copy of the input
        x = n

        while x > 0:
            x, d = divmod(x, 10) # we 
            if d == 0 or n % d > 0:
                return False
        return True
