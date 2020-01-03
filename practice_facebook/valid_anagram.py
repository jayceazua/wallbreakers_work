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
from collections import Counter
def valid_anagram(s, t):
  if len(s) != len(t):
    return False
  # solution 1
  s = Counter(s)
  t = Counter(t)
  return len(s - t) == 0
  # solution 2
  # counts = [0]*26

  # for index, letter in enumerate(s):  # O(n) time complexity
  #     counts[ord(letter) - ord('a')] += 1
  #     counts[ord(t[index]) - ord('a')] -= 1

  # # check that all the counts in the array are equal to 0
  # for count in counts:  # O(n) time
  #     if count != 0:
  #         return False
  # return True
