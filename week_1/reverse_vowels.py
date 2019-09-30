"""
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:

Input: "hello"
Output: "holle"
Example 2:

Input: "leetcode"
Output: "leotcede"
Note:
The vowels does not include the letter "y".
"""


class Solution:
    def reverseVowels(self, s: str) -> str:
        # set of vowels for constant lookup
        lookup_vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        "leetcode"
        # vowel : indices set
        vowels = []
        # vowels 1->e, 2->e, 5->0, 7->e
        for index, letter in enumerate(s):
            if letter in lookup_vowels:
                vowels.append((index, letter))
        s = list(s)
        for index, value in enumerate(vowels):
            s.pop(value[0])
            s.insert(value[0], vowels[-index-1][1])

        return "".join(s)
