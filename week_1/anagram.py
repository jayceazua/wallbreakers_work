"""
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counts = [0]*26

        for index, letter in enumerate(s):  # O(n) time complexity
            counts[ord(letter) - ord('a')] += 1
            counts[ord(t[index]) - ord('a')] -= 1

        # check that all the counts in the array are equal to 0
        for count in counts:  # O(n) time
            if count != 0:
                return False
        return True

#         s_histo = self.create_histo(s) # O(n) time and space

#         for letter in t:
#             if not letter in s_histo:
#                 return False

#             if letter in s_histo:
#                 if s_histo[letter] == 1:
#                     s_histo.pop(letter)
#                 else:
#                     s_histo[letter] -= 1
#         return True

        # edge/corner case unicode characters
#     def create_histo(self, word):
#         histo = {}

#         for letter in word:
#             if letter in histo:
#                 histo[letter] += 1
#             else:
#                 histo[letter] = 1

#         return histo
