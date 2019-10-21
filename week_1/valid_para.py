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
        # order matters 
        # we need to see the corresponding character 
        # 



# def is_Valid(s: str) -> bool:

#     if len(s) % 2 == 0:
#         return False

#     stack = []  # }

#     for char in s:
#         # check if it is a opening bracket
#         if char in "([{":
#             stack.append(char)

#         elif char == ")" and len(stack) != 0 and stack[-1] == "(":
#             stack.pop()

#         elif char == "}" and len(stack) != 0 and stack[-1] == "{":
#             stack.pop()

#         elif char == "]" and len(stack) != 0 and stack[-1] == "[":
#             stack.pop()

#         else:
#             return False

#     return len(stack) == 0
