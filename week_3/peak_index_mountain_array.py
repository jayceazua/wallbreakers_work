"""
Let's call an array A a mountain if the following properties hold:

A.length >= 3
There exists some 0 < i < A.length - 1 such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
Given an array that is definitely a mountain, return any i such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1].

Example 1:

Input: [0,1,0]
Output: 1
Example 2:

Input: [0,2,1,0]
Output: 1
Note:

3 <= A.length <= 10000
0 <= A[i] <= 10^6
A is a mountain, as defined above.
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        # basecase
        if n == 0:
            return 1.0

        # inductive case
        if n < 0:
            return 1/self.myPow(x, -n)

        elif n % 2 == 0:
            return self.myPow(x*x, n // 2)

        elif n % 2 == 1:
            return x * self.myPow(x*x, n // 2)
