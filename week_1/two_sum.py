"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # create a set for the numbers assuming that there are no duplicates
        compliments = {}

        for index, num in enumerate(nums):  # O(n)
            compliments[num] = index

        for index, num in enumerate(nums):  # O(n)
            comp = target - num
            if comp in compliments:  # O(1)
                if compliments[comp] == index:
                    continue
                return [index, compliments[comp]]
        # naive solution
        # for i, n in enumerate(nums): # O(n^2)
        #     for j, m in enumerate(nums):
        #         if i == j:
        #             continue
        #         if n + m == target:
        #             return [i, j]
