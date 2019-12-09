# Suppose we have some input data describing a graph of relationships between parents and children over multiple generations. The data is formatted as a list of (parent, child) pairs, where each individual is assigned a unique integer identifier.

# For example, in this diagram, 6 and 8 have a common ancestor of 4.

#          14  13
#          |   |
# 1   2    4   12
#  \ /   / | \ /
#   3   5  8  9
#    \ / \     \
#     6   7     11

# parentChildPairs1 = [
#     (1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5),
#     (4, 8), (4, 9), (9, 11), (14, 4), (13, 12), (12, 9)
# ]

# Write a function that takes the graph, as well as two of the individuals in our dataset, as its inputs and returns true if and only if they share at least one ancestor.

# Sample input and output:

# hasCommonAncestor(parentChildPairs1, 3, 8) => false
# hasCommonAncestor(parentChildPairs1, 5, 8) => true
# hasCommonAncestor(parentChildPairs1, 6, 8) => true
# hasCommonAncestor(parentChildPairs1, 6, 9) => true
# hasCommonAncestor(parentChildPairs1, 1, 3) => false
# hasCommonAncestor(parentChildPairs1, 7, 11) => true
# hasCommonAncestor(parentChildPairs1, 6, 5) => true
# hasCommonAncestor(parentChildPairs1, 5, 6) => true

# Additional example: In this diagram, 4 and 12 have a common ancestor of 11.

#         11
#        /  \
#       10   12
#      /  \
# 1   2    5
#  \ /    / \
#   3    6   7
#    \        \
#     4        8
#
# parentChildPairs2 = [
#     (11, 10), (11, 12), (10, 2), (10, 5), (1, 3),
#     (2, 3), (3, 4), (5, 6), (5, 7), (7, 8),
# ]

# hasCommonAncestor(parentChildPairs2, 4, 12) => true
# hasCommonAncestor(parentChildPairs2, 1, 6) => false
# hasCommonAncestor(parentChildPairs2, 1, 12) => false

# n: number of pairs in the input

parent_child_pairs_1 = [
    (1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5),
    (4, 8), (4, 9), (9, 11), (14, 4), (13, 12), (12, 9)
]


parent_child_pairs_2 = [
    (11, 10), (11, 12), (10, 2), (10, 5), (1, 3),
    (2, 3), (3, 4), (5, 6), (5, 7), (7, 8)
]


def hasCommonAncestor(parentChildPairs2, child1, child2):
    members = get_unique_family(parentChildPairs2)
    get_ancestors(members, parentChildPairs2)
    get_more_ancestors(members)
    print(len(members[child1] & members[child2]) > 0)
    return len(members[child1] & members[child2]) > 0


def get_ancestors(members, pairs):
    for parent, child in pairs:
        if child in members:
            members[child].add(parent)
            members[child] = members[child] | members[parent]


def get_more_ancestors(members):
    for member, ancestors in members.items():
        for ancestor in ancestors:
            members[member] = members[member] | members[ancestor]


def get_unique_family(pairs):
    unique = {}  # O(n) space

    for parent, child in pairs:  # O(n) runtime
        if parent not in unique:
            unique[parent] = set()
        if child not in unique:
            unique[child] = set()

    return unique


# hasCommonAncestor(parent_child_pairs_1, 3, 8) # => false
# hasCommonAncestor(parent_child_pairs_1, 5, 8) # => true
# hasCommonAncestor(parent_child_pairs_1, 6, 8) # => true
# hasCommonAncestor(parent_child_pairs_1, 6, 9) # => true
# hasCommonAncestor(parent_child_pairs_1, 1, 3) # => false
# hasCommonAncestor(parent_child_pairs_1, 7, 11) # => true
# hasCommonAncestor(parent_child_pairs_1, 6, 5) # => true
# hasCommonAncestor(parent_child_pairs_1, 5, 6) # => true
# hasCommonAncestor(parent_child_pairs_2, 4, 12) #=> true
# hasCommonAncestor(parent_child_pairs_2, 1, 6) #=> false
# hasCommonAncestor(parent_child_pairs_2, 1, 12) #=> false
hasCommonAncestor(parent_child_pairs_2, 6, 4)  # => true

# hasCommonAncestor(parent_child_pairs_2, 4, 12) # => true
# hasCommonAncestor(parent_child_pairs_2, 1, 6)  # => false
# hasCommonAncestor(parent_child_pairs_2, 1, 12) # => false

# Main function here - problem 1
# def findNodesWithZeroAndOneParents(parentChildPairs):
#     family = get_unique_family(parentChildPairs) # O(n) runtime/ space
#     get_parents(family, parentChildPairs) # O(n) runtime


#     no_parents = []
#     one_parent = []

#     for member, value in family.items():
#         if value == 0:
#             no_parents.append(member)
#         elif value == 1:
#             one_parent.append(member)

#     return [no_parents, one_parent]


# def get_parents(family, pairs):

#     for _, child in pairs:
#         if child in family:
#             family[child] += 1

# def get_unique_family(pairs):
#     unique = {} # O(n) space

#     for parent, child in pairs: # O(n) runtime
#         if parent not in unique:
#             unique[parent] = set()
#         if child not in unique:
#             unique[child] = set()

#     return unique
