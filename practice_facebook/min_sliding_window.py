"""
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
"""


def minWindow(s, t):
    """
      clarifying questions:
        - can there be duplicates in either s or t?
          - reason we should ask this is because this will determine if we use a set or a Counter dictionary(hashtable) 
        - can s or t be empty
        - what should we return if nothing is found -> ""
        - what if t is greater than s
        - what if only a few characters of t is found in s; what should be returned.
        - what if we have the same length size; which should we return?
        - can they be in any order?
        - can they have different characters between them
        - we can see the input being capital alphabet letters, can we assume that is the case of all other inputs?
          - is it possible to have any other type like ints, floats, etc.
          - possible to have special characters like &^%$ or lowercase characters?

      Algorithm:
       - we will have a sliding window grow in size until we hit all the characters in t
       - we will have a counter dict as our look up table and each time we find a character 
          that is in t we will decrement the count by 1 and once it reaches to 0 we delete it from the counter dict.
       - we have to consider that once end or start reaches the end we have reached the end of our algorithm. 
       - we will have a consistent checker checking the minimum length of the substring 
          and replace the answer with the smallest find.
       - once we reach the end we return the answer we have been storing.
       - j will continuously reset back to the starting point of i

    """
    if not s or not t:
        return ""

    res = ""
    dic = Counter(t)

    cnt = 0
    wind = len(s) + 1
    l = 0
    for r in range(0, len(s)):
        dic[s[r]] -= 1
        if dic[s[r]] >= 0:
            cnt += 1

            while cnt == len(t):
                if r - l + 1 < wind:
                    wind = r - l + 1
                    res = s[l:r+1]

                dic[s[l]] += 1
                if dic[s[l]] > 0:
                    cnt -= 1

                l += 1

    return res
