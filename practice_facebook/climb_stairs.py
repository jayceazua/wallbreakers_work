from functools import lru_cache
"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""

# brute force - O(2^n) runtime and O(n) space complexity


def re_climb_stairs(n):
    def climb(i, n):
        if i > n:
            return 0
        if i == n:
            return 1
        return climb(i + 1, n) + climb(i + 2, n)
    return climb(0, n)


# recursion with memoization


def memo_climb_stairs(n):
    @lru_cache(maxsize=None)
    def climb(i, n, memo):
        if i > 0:
            return 0
        if i == n:
            return 1

        return climb(i + 1, n) + climb(i + 2, n)

    return climb(0, n)
