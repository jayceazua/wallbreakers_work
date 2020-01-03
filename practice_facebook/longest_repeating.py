"""
Given a string s that consists of only uppercase English letters, you can perform at most k operations on that string.

In one operation, you can choose any character of the string and change it to any other uppercase English character.

Find the length of the longest sub-string containing all repeating letters you can get after performing the above operations.

Note:
Both the string's length and k will not exceed 104.

Example 1:

Input:
s = "ABAB", k = 2

Output:
4

Explanation:
Replace the two 'A's with two 'B's or vice versa.
 

Example 2:

Input:
s = "AABABBA", k = 1

Output:
4

Explanation:
Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
"""

from collections import defaultdict


def characterReplacement(s, k):
    if not s:
        return 0

    char_counts = defaultdict(int)
    max_count = float('-inf')
    start = 0

    for end, char in enumerate(s):
        char_counts[char] += 1
        max_count = max(max_count, char_counts[char])

        if end - start + 1 - max_count > k:
            char_counts[s[start]] -= 1
            start += 1

    return end - start + 1
