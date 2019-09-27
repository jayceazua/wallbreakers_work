"""
Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Note: In the string, each word is separated by single space and there will not be any extra space in the string.
"""


class Solution:
    def reverseWords(self, s: str) -> str:

        s_split = s.split()

        for index, word in enumerate(s_split):
            s_split.pop(index)
            s_split.insert(index, word[::-1])

        return " ".join(s_split)
