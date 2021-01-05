# [(7, 10), (12, 14)] -> 1
# [(7, 10), (12, 14), (5, 15), (13, 14), (16, 18), (20, 21)] -> 1


"""
check if it is empty
return 0 
-----
count -> 1 -> 2

start = [7, 12, 5, ... n-1] 

            
ongoing = 3

ongoing = 1
4 rooms << return this
                        s
start = [5, 7, 12, 13, 20] # O(n log n)

end =   [10, 14, 14, 15, 22]
                         e

return ongoing -> 3


[(7, 10), (12, 14), (5, 15), (13, 14), (16, 18), (20, 21)]


if s >= e:
  count++
end =   [10, 14, 15, ... n-1]


Complexity of the algorithm:
O(n) space
O(n log n) time 
"""


def how_many_meeting_rooms(meetings):
    """
        used_rooms = 0

        ongoing = 3
    
                                    s
        start = [5, 7, 12, 13, 20, 20, 21, 21, 21, 22]

        end =   [10, 14, 14, 15, 24, 24, 24, 24, 24, 24]
                                 e
    """
    if not meetings:
        return 0

    rooms = 0  # always be one after this point
    start_times = sorted([times[0] for times in meetings])  # O(n^2 log n)
    end_times = sorted([times[1] for times in meetings])

    length = len(meetings)

    start_ptr, end_ptr = 0, 0

    while start_ptr < length:

        while start_times[start_ptr] >= end_times[end_ptr]:
            rooms -= 1
            end_ptr += 1

        rooms += 1
        start_ptr += 1

    return rooms


if __name__ == "__main__":
    # test cases here
    input1 = [(7, 10), (12, 14)]
    input2 = [(7, 10), (12, 14), (5, 15), (13, 14), (16, 18), (20, 21)]
    print(how_many_meeting_rooms(input1))
    print(how_many_meeting_rooms(input2))
