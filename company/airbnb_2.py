# solve this problem using sets
def highest_concat(A):

    unique_words = []  # there can still be words with similar letters

    # gets all unique words in the input array of strings
    for word in A:  # O(n)
        if len(word) == len(set(word)):
            unique_words.append(set(word))  # O(n)
    if len(unique_words) == 0:
        return 0

    highest_combo = set()
    turn_combo = set()
    for word_one in unique_words:  # O(n)

        for word_two in unique_words:  # O(n)
            # cannot be same word to compare
            if word_one == word_two:
                continue

            # check if there is an intersection among the words
            has_letter = len(word_one & word_two) != 0
            in_turn_combo = len(turn_combo & word_two) != 0

            if has_letter or in_turn_combo:
                continue
            turn_combo = (turn_combo | word_two)

        turn_combo = (turn_combo | word_one)

        if len(turn_combo) > len(highest_combo):
            highest_combo = turn_combo
        # set the turn_combo back to an empty set
        turn_combo = set()
# return the highest combo
    return len(highest_combo)


# Test cases:
    # ["abc", "befg", "exy", "wrtnma"]
    # different combinations
    # 6 x (abc, exy)
    # 10 y (befg, wrtnma)
    # 9 x (exy, wrtnma)


A = ["abc", "befg", "exy", "wrtnma"]
print(highest_concat(A))  # 10
