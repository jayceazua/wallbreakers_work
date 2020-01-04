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


def valid_palindrome(s):

    if not s:
        return True

    i = 0
    j = len(s) - 1

    while i <= j:
        start = s[i]
        end = s[j]

        if start.isalnum() and end.isalnum():
            if start != end:
                return False
            i += 1
            j -= 1

        elif not start.isalnum():
            i += 1
        elif not end.isalnum():
            j -= 1
    return True
