from collections import Counter
"""
Given a list of daily temperatures T, return a list such that, 
for each day in the input, tells you how many days you would have to wait until a warmer temperature. 
If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], 
your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].
"""


def dailyTemperatures(T):
    if not T:
        return

    days = [0] * len(T)
    temps_stack = []

    for current_day, current_temp in enumerate(T):
        while temps_stack and temps_stack[-1][0] < current_temp:
            _, day = temps_stack.pop()
            days[day] = current_day - day

        temps_stack.append((current_temp, current_day))
    return days


# ryan mock interview


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
