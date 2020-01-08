"""
Input:

 s = "BAERTLLQOBONSEIWBEOBNBLAOLLOO"

 {'B: 2,
    'A': 2,
    'L': 5


 }
 # generalized
 k = "BALLOON"

Output:
    int ->  # of times BALLOON

"""

from collections import Counter  # ask to use this

# jumped into coding without having a clear path of a solution


def num_occ(s, k):  # O(n) runtime and O(n) space
    if not s or not k:
        return 0

    s_histo = Counter(s)  # O(n) runtime/ space
    k_histo = Counter(k)

    num = float('inf')

    for char, count in k_histo.items():  # BALLOON

        if char not in s_histo:
            return 0

        make = s_histo[char]  # 5
        potential = make // count  # 5

        num = min(num, potential)

    return num


# print(num_occ("BAERTLLQOBONSEIWBEOBNBLAOLLOO", "BALLOON"))
# print(num_occ("           ", " ")) # 11
print(num_occ("  ", " "))  # 0
# print(num_occ("BAERTLLQOBONSEIWBEOBNBLAOLLOO", "BALLOON"))
