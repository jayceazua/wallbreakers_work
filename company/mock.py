
"""
Given an array of integers, move all zeros to the front of the array.

Example:
  input:
    [0,1,0,2,4,5]

  output:
    [0,0,1,2,4,5]



Walk through example:
  [0, 0, 5, 2, 4, 5, 0, 0]


"""


def opt_move_zeros(nums):  # O(n) runtime; O(z + nz) space
    zeros = []  # O(z) space linear
    non_zeros = []  # O(nz)
    for index, num in enumerate(nums):  # O(n) linear runtime
        if num == 0:
            zeros.append(num)
        else:
            non_zeros.append(num)

    nums[:] = zeros + non_zeros
    del zeros
    del non_zeros


def br_move_zeros(nums):  # O(n^2) - squared; power of 2
    """
      input:
        List[ints]
      output:
        no output, because I am doing it in-place. No extra space created.
    """

    for index, num in enumerate(nums):  # O(n)
        if num == 0:
            nums.pop(index)  # O(n)
            nums.insert(0, num)  # O(n)
