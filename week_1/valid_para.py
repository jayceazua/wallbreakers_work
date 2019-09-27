"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        lookup = {
            "(": ")",
            "[": "]",
            "{": "}"
        }

        for character in s:

            if character in lookup:
                stack.append(character)

            elif len(stack) == 0 or lookup[stack.pop()] != character:
                return False

        return len(stack) == 0
