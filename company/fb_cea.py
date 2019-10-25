'''
Count distinct characters in every window of size k 

Given a string and an integer k, print the of count of distinct characters in all windows of size k.

Example:
Input:  
  s = "abacdbc"
  k = 4

Output:
3      //   "abac" 
4      //   "bacd"
4      //   "acdb"
3      //   "cdbc"


Edge Cases:
K > len(s) -> nothing
---
K = 0 -> nothing
K = 1 -> len(s)
K == len(s) -> len(Counter(s))

 - what if K is negative,
 - a float; do we get the ceiling or floor of the float?

hashtable example

{ 
    'c' : 2,
    'd' : 1,
    'b' : 1,
}

'''


from collections import Counter


# optimial solution
def opti_unique_char(s, k):

    # edge cases
    if k <= 0 or k > len(s):
        return
        
    if k == 1:
        return len(s)

    if k == len(s):
        print(len(Counter(s)))

    current_window = Counter(s[:k])

    for index in range(0, len(s) - k - 1):  # 0 1 2

        # remove the first char of the window
        if current_window[s[index]] == 1:
            del current_window[s[index]]

        else:
            current_window[s[index]] -= 1

        # add the new char
        if current_window.get(s[index + k], False):  # 2 + 4 = 6
            current_window[s[index + k]] += 1

        else:
            current_window[s[index + k]] = 1

        print(len(current_window))


# brute force
def bru_unique_char(s, k):

    if k > len(s):
        return

    if k == len(s):
        print(len(set(s)))


    for index in range(len(s) - k):  # O(n)
        # O(n) (a,b,c) -> (b, a, c, d) -> (a, c, d, b) -> (c, d, b, c)
        unique = set(s[index: index + k])
        print(len(unique))  # 3, 4, 4, 3
