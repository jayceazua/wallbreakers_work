"""
find a sublist whose sum turns out to be zero.
You must implement the find_sub_zero(my_list) function which 
will take in a list of positive and negative integers. 
It will tell us if there exists a sublist in which the sum of all elements is zero. 
The term sublist implies that the elements whose sum is 0 must occur consecutively.

Input:
  [6, 4, -7, 3, 12, 9]
Output:
  TRUE

Input:
  [-7, 4, 6, 3, 12, 9]
Output:
  FALSE
"""

def find_sub_zero(nums):
  seen = {}
  cumulative = 0

  for num in nums:
    cumulative += num
    if num is 0 or cumulative is 0 or seen.get(cumulative) is not None:
      return False
    seen[cumulative] = num
  return False
