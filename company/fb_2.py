def find_num(nums, target):

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
  nums_hash = {}
  for index, num in enumerate(nums): # O(n) runtime and space
    nums_hash.setdefault(nums, index)
  if nums_hash.get(target, False): # O(1) runtime and space
    return nums_hash[target]
  return None

  # Optimized Solution - using binary search







if __name__ == "__main__":
#        L     P     R
  arr = [3, 4, 5, 1, 2]
  target = 4
  print(find_num(arr, target))
