"""
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:

Input: pattern = "abba", str = "dog cat cat dog"
Output: true
Example 2:

Input:pattern = "abba", str = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false
Example 4:

Input: pattern = "abba", str = "dog dog dog dog"
Output: false
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters that may be separated by a single space.
"""


class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        t = str.split()
        if len(t) != len(pattern):
            return False

        dic = {}
        used_words = set()
        for i in range(len(t)):
            if pattern[i] not in dic:
                if t[i] not in used_words:
                    dic[pattern[i]] = t[i]
                    used_words.add(t[i])
                else:
                    return False
            elif dic[pattern[i]] != t[i]:
                return False
        return True
