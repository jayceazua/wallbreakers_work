"""
Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.
 

Example 1:

Input: "USA"
Output: True
 

Example 2:

Input: "FlaG"
Output: False
"""


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
      return word.isupper() or word.islower() or word.istitle()
        # checks that all the letters in the word are upper case
        # if word.isupper():
        #     return True
        # # checks that all the letters in the word are lower case
        # if word.islower():
        #     return True

        # found = False
        # for i in range(len(word)):
        #     is_upper = word[i].isupper()

        #     if is_upper and found == False and i == 0:
        #         found = True

        #     elif found == False and is_upper:
        #         return False
        #     elif is_upper and found:
        #         return False

        # return True


# usage of characters are correct:
    # all letters are capital
    # all letters are not capital
    # the first letter in the word is capital
