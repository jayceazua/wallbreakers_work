"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
"""


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # alphabet_lower = [0]*26
        ans = ""
        if len(strs) == 0 or strs == None:
            return ans
        # naive solution

        # loop through each letter of the first word
        for i in range(len(strs[0])):
            # go through each word after the first word
            for _, word in enumerate(strs, start=1):
                # check if the current index is greater than or equal to the shorest word
                    # also check if the current index letter of the first word is not equal to the index letter of the otheer words
                if i >= len(word) or strs[0][i] != word[i]:
                    # break from the loop and return what we current have
                    return ans
            # otherwise add the letter into the longestCommon prefix variable
            ans += strs[0][i]

        # if we loop through the entire first word then the entire first word is a prefix
        return ans
