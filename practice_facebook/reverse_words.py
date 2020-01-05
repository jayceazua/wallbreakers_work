"""
Given an input string, reverse the string word by word.

 

Example 1:

Input: "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: "  hello world!  "
Output: "world! hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
 

Note:

A word is defined as a sequence of non-space characters.
Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
You need to reduce multiple spaces between two words to a single space in the reversed string.
 

Follow up:

For C programmers, try to solve it in-place in O(1) extra space.
"""


def reverseWords(words):
    if not words:
        return words

    return ' '.join(words.strip().split()[::-1])
#       left = 0
#       right = len(words) - 1
#       # remove leading spaces
#       while left <= right and words[left] == ' ':
#         left += 1
#       # remove trailing spaces
#       while left <= right and words[right] == ' ':
#         right -= 1
#       d, word = deque(), []
#       # push word by word in front of deque
#       while left <= right:
#         if words[left] == ' ' and word:
#           d.appendleft(''.join(word))
#           word = []
#         elif words[left] != ' ':
#           word.append(words[left])
#         left += 1
#       d.appendleft(''.join(word))
#       return ' '.join(d)
