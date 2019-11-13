def search(nums, target):

  # naive solution 1
  # for index, num in enumerate(sorted(nums)): # O(n log n) + O(n)
  #   if num == target:
  #     return index
  # return None

  # naive solution 2
  # try:
  #   return nums.index(target) # O(n)
  # except ValueError:
  #   return None

  # naive solution 3
  # for index, num in enumerate(nums): # O(n)
  #   if num == target:
  #     return index
  # return None

  # naive solution 4
  # nums_hash = {}
  # for index, num in enumerate(nums): # O(n) runtime and space
  #   nums_hash.setdefault(nums, index)
  # if nums_hash.get(target, False): # O(1) runtime and space
  #   return nums_hash[target]
  # return None

  # Optimized Solution - finding the smallest element's index then using binary search
  if len(nums) == 0:
      return -1
  # O(log n) - find the smallest element in the given array of integers
  smallest_index = get_rotated_index(nums, 0, len(nums) - 1)

  left = 0
  right = len(nums) - 1

  # how do we know which side to binary search on...
  if target >= nums[smallest_index] and target <= nums[right]:
    # search on the right
      left = smallest_index
  else:
    # otherwise search on the left
      right = smallest_index

  # O(log n) - perform a regular binary search with an al
  return binary_search(nums, left, right, target)

  # Optimized Solution - one pass binary search
  # start = 0
  # end = len(nums) - 1
  # while start <= end:
  #     # prevents integer overflow in other languages
  #     mid = start + (end - start) // 2
  #     # found the answer
  #     if nums[mid] == target:
  #         return mid
  #     elif nums[mid] >= nums[start]:
  #         if target >= nums[start] and target < nums[mid]:
  #             end = mid - 1
  #         else:
  #             start = mid + 1
  #     else:
  #         if target <= nums[end] and target > nums[mid]:
  #             start = mid + 1
  #         else:
  #             end = mid - 1
  # return -1

#regular binary search here
def binary_search(nums, left, right, target):
  while left <= right:
      mid = left + (right - left) // 2
      if nums[mid] == target:
          return mid
      if nums[mid] < target:
          # look towards the right side of the array
          left = mid + 1
      elif nums[mid] > target:
          # look towards the left side of the array
          right = mid - 1
  return -1

def get_rotated_index(nums, left, right):
    # first we must find the smallest element in the array
    # the smallest element in the array should be our
    # way of knowing if we should search left or right
  while left < right:
      mid = left + (right - left) // 2
      
      if nums[mid] > nums[right]:
        # this tells us that the smallest will be on the right side of the array
          left = mid + 1
      else:
        # otherwise we will know that the smalllest is on the left side of the array
          right = mid
  return left



if __name__ == "__main__":
#        L     P     R
  arr = [4, 5, 6, 7, 0, 1, 2, 3]
  target = 1
  print(search(arr, target))
