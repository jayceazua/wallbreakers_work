# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A, K, L):
    # write your code in Python 3.6
    """
        Test case:
        A = [10,19,15]
        K = 2
        L = 2
        
        Test case:
        
        A = [6, 2, 4, 6, 3, 2, 7, 4]
        K = 3; 
        L = 2
        
        Test case:
        A = [4, 5, 6, 5, 9, 8, 10, 45, 7]
        K = 2
        L = 2
        current solution = 110
        real answer = 72
        
        

    """
    # create a subarray window based on K or L
    # solving the edge case
    if K + L > len(A):
        return -1

    # this just solves for maximum sum subarray of size K or L
    # need to return the combos to make sure they are not picking from the samee tree...
    # alice = max_subarray_of(A, K)
    # bob = max_subarray_of(A, L)

    # return alice + bob

    alice = get_all_combos(A, K)
    bob = get_all_combos(A, L)

    return get_max_sum(alice, bob)

    # return get_max_sum(alice, bob)


def get_max_sum(alice, bob):
    """
    given inputs:
    Alice: [(11, {0, 1, 2}), (11, {1, 2, 3}), (13, {2, 3, 4}), (11, {3, 4, 5}), (12, {4, 5, 6}), (13, {5, 6, 7})]
    Bob: [(7, {0, 1}), (5, {1, 2}), (10, {2, 3}), (9, {3, 4}), (5, {4, 5}), (9, {5, 6}), (11, {6, 7})]
    
    !warning that alice and bob might not have the same length of combinations!
    """
    possible_sum = []
    for alice_total, alice_combo in alice:
        for bob_total, bob_combo in bob:
            # check for intersection
            if len(alice_combo & bob_combo) != 0:
                continue
            possible_sum.append(alice_total + bob_total)
    return max(possible_sum)


# get all combinations
def get_all_combos(A, K):
    """
    returns a tuple of the sum and the index combo in a set
    setting it up for constant look up
    """
    n = len(A)
    # print(n)
    results = []
    combo = set()
    total = 0
    for i in range(n-(K-1)):
        for j in range(i, i+K):
            total += A[j]
            combo.add(j)
        results.append((total, combo))
        total = 0
        combo = set()
    return results


