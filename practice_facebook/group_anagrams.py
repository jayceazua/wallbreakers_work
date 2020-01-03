"""
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
"""


from collections import defaultdict


def groupAnagrams(words):

    grouped_anagrams = defaultdict(list)

    for word in words:  # O(n) runtime to go through each
        grouped_anagrams[tuple(sorted(word))].append(word)  # O(n) runtime to sort/ O(1) to append

    return grouped_anagrams.values()  # O(n) time and space
