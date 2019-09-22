"""
Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition.

 

Example 1:

Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
 

Note:

1 <= A.length <= 5000
0 <= A[i] <= 5000
"""


class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        # it is passed as a reference
        nums = A  # this does not make a copy but it is a reference of the input array
        # nums = A.copy() # this makes a copy of the array .

        for index, num in enumerate(nums):
            if num % 2 == 0:
                nums.pop(index)
                nums.insert(0, num)
            # else: < - this was not even needed to use...
            #     nums.pop(index)
            #     nums.append(num)

        return A
