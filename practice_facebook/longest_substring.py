"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


def longest_substring(input_string):
  n = len(input_string)
  if not input_string:
    return n
  
  max_size = float('-inf')
  window = set()

  i = 0
  j = 0

  while i < n and j < n:
    if input_string[j] not in window:
      max_size = max(max_size, j - i)
      j += 1
      window.add(input_string[j])
    else:
      window.remove(input_string[i])
      i += 1
      
  return max_size
  
