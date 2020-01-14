"""
A
B C
D
D B C A
C - D

results = [2, 1, 3, 5]
no_depend = [4, 5]
                                          i
Packages =     int nums1 = {1, 2, 3,  4,  5, 5}  
                                          j
Dependencies = int nums2 = {3, 3, 5,  4, -1, -1}

Num of packages = 10 


4 5 3 2 1 6n 7n 8 9 10

installment - dependencies
1 - 3
2 - 3
3 - 5
4 

3 - 3



1 - 2
2 - 3
3 - 1

nums1 = [121212121212]
nums1 = [212121212121]
deadlock situation ... cycle

class Vertex:
    def __init__(self, val):
        self.val = val
        self.neighbors = []
        
def Graph:
    pass
        
"""

# packages = {1, 2, 3, 4 , 5}
# dependencies = {3, 3, 5, -1, -1}
# numOfPackages = 5


def find_installation_path(packages, dependencies, numOfPackages):
    if not packages and not dependencies:
        return []

    result = deque()
    no_depend = []

    installed = set()  # check if already installed

    for i in range(len(packages)):

        package = packages[i]
        dependa = dependencies[i]

        if package == dependa:
            return []

        elif dependa == -1 and dependa not in installed:
            no_depend.append(package)

        # toplogical sort
        elif package not in installed:
            result.append(packahe)

        elif dependa not in installed:
            result.appendleft(dependa)

    return result.extend(no_depend)  # O(n)


'''                    i    
doordash_hours =   [(9, 12), (14, 17), (21, 23)]
                                j
restaurant_hours = [(8, 10), (11, 22)]

     |   | 
=> [(9, 10), (11, 12), (14, 17), (21, 22)]


[(9, 12)]
[(8, 10)]

max(9, 8) => 9
min(12, 10)

result = [(9, )]
'''
'''
def get_dd_hours(day, city): O(n) + n log n
    something
    
def get_store_hours(day, store):
    something
def is_open(store):
    dd_hrs = get_dd_hours(today, store.city) <- O(n) runtime/ space
    store_hrs = get_store_hours(today, store) <- O(n) runtime /space
    
    ## sort? O(n log n) runtime // O(n) space
    
    if overlapping_intervals(dd_hrs, store_hrs):
        return true
    return false
'''


def sort_inputs(dd, rest):  # O(n + m) runtime

    if not rest or not dd:  # edge cases
        return []

    ans = []  # append
    i = 0  # dd
    j = 0  # rest

    result = [None]*2  # convert to tuple

    while i < len(dd) and j < len(rest):
        # easier to read- get individual intervals
        interval_dd = dd[i]
        interval_rest = rest[j]

        # setting the tuple interval
        result[0] = max(interval_dd[0], interval_rest[0])
        result[1] = min(interval_dd[1], interval_rest[1])

        # reset the result
        ans.append(tuple(result))
        result = [None]*2

        # deciding when to increment
        if interval_dd[1] >= interval_rest[1]:  # end time checks
            j += 1
        else:
            i += 1  # increment i - doordash

    # return the answer
    return ans


print(sort_inputs([(9, 12), (14, 17), (21, 23)], [(8, 10), (11, 22)]))
