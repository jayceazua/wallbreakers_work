"""
find the celebrity
"""


def knows(candidate, person):  # O(n) runtime and O(1) space
    pass


def find_celebrity(n):
    celebrity = 0

    # do an initial loop
    for i in range(1, n):  # O(n)
        if knows(celebrity, i):
            celebrity = i

    # do another loop
    for i in range(n):  # O(n)
        # oonly if current person is not the celebrity or the celebrity knows the person
            # or current person does not know the celebrity, then there is no celebrity
        if i != celebrity and knows(celebrity, i) or not knows(i, celebrity):
            return -1

    return celebrity
