"""
Given an array of integers, remove duplicates

Ex:
input: [3, 4, 5, 6, 7, 8, 8, 11, 23, 3]

"""


def delete_duplicates(A):
    if not A:
        return 0

    write_index = 1

    for i in range(1, len(A)):
        if A[write_index - 1] != A[i]:
            A[write_index] = A[i]
            write_index += 1
    return write_index
