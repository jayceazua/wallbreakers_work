"""
Given an array of integers arr, a positive integer k, and an integer s, 
  your task is to find the number of non-empty contiguous subarrays 
  with length not greater than k and with a sum equal to s.

Example:

For arr = [1, 0], k = 2, and s = 1, the output should be 2

 - There is 1 subarray among the contiguous subarrays of length 1 with sum equal to s = 1, and it is [1],
 - There is 1 subarray among the contiguous subarrays of length 2 with sum equal to s = 1. and it is [1, 0].
 - So the answer is 2.

For arr = [1, 2, 4, -1, 6, 1], k = 3, and s = 6, the output should be 3.
  - There is 1 subarray among the contiguous subarrays of length 1 with sum equal to s = 6, and it is [6],
  - There is 1 subarray among the contiguous subarrays of length 2 with sum equal to s = 6, and it is [2, 4],
  - There is 1 subarray among the contiguous subarrays of length 3 with sum equal to s = 6, and it is [-1, 6, 1],
  - So the answer is 3


Input/ Output

 - [execution time limit] 4s

[input] array.integer arr
  An array of integers.
  Guaranteed Constraints:
  2 <= arr.length <= 10**5
  -10**9 <= arr[i] <= 10**9

[input] integer k
  A positive integer denoting the maximal length of the contiguous subarrays we'll be considering.
  Guaranteed Constraints
  1 <= k <= arr.length

[input] integer64 s
 An integer representing the sum we're looking for within the contiguous subarrays. 
 Note, that this integeer may not fit in 32-bit type and thus provided in a 64-bit type.

 Guaranteed Constraints:
 -10**11 <= s <= 10**11

[ouput] integer64
 - The number of the contiguous subarray with the given sum.

"""


arr = [1, 2, 4, -1, 6, 1]
k = 3
s = 6

def foo_bar(arr, k, s): # O(n*k)
  window = 1
  count = 0
  while window <= k:

    for index in range(len(arr)):
      total = sum(arr[index:window+index])

      if total == s:
        count += 1

    window += 1

  return count 


print(foo_bar(arr, k, s))
