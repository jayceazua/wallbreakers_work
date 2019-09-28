"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:  # O(n/2)
       # clean the string being passed in
        if s == "":
            return True

            # Kevin's/ Ricky's solution
        i = 0
        j = len(s) - 1

        while i < j:
            # check for i which is the beginning
            while i < j and not s[i].isalnum():
                i += 1
            # check for j which is the end
            while i < j and not s[j].isalnum():
                j -= 1

            if i < j and s[i].lower() != s[j].lower():
                return False
            # increment and decrement i and j after all the checks
            i += 1
            j -= 1

        return True

        # Jayce's solution
#         s = self.clean_string(s) # O(n) time/ space <- pre-processing input data
#         r_string = self.reverse_string(s) # O(n) time and space

#         return s == r_string

    # pre-processing input data
#     def reverse_string(self, s): # O(2n) -> O(n)
#         stack = []
#         reversed_str = ""
#         for char in s: # O(n) time
#             stack.append(char)

#         for _ in range(len(stack)): # O(n) time
#             reversed_str += stack.pop()
#         return reversed_str

#     # pre-process input data
#     def clean_string(self, dirty_string):
#         clean = ""
#         for char in dirty_string:
#             if char.isalpha() or char.isalnum():
#                 clean += char.lower()
#         return clean
