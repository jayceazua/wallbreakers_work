"""

input: arr 
[int, int, int]
houses on a row and they have gold

problem - i cannot rob houses next to each other

counter_one = 0 -> 1 -> 5 -> 6
counter_two = 0 -> 3 + 5

path_one = 0 + 2
path_two = 1 + 2
 
 
[1-po, 3-pt, 4, 5, 6] = 11



[100, 1, 1, 100, 1]

"""

# O(2^n)
def rewardFromStartingHere(index, arr):
    if index >= len(arr):
        return 0
    # robbing this house
    path_one = arr[index] + rewardFromStartingHere(index + 2, arr)
    # not robbing this house
    path_two = rewardFromStartingHere(index + 1, arr)

    return max(path_one, path_two)

# O(n)
def memoizedRob(arr):
    results = []  # we will append results as they come in

    for index, gold in enumerate(arr):
        path_one = gold + results[index - 2] if index - 2 >= 0 else gold
        path_two = results[index - 1] if index - 1 >= 0 else 0
        results.append(max(path_one, path_two))

    return results[-1]

# Driver Code...
houses = [100, 1, 1, 100, 1]
print(memoizedRob(houses))
