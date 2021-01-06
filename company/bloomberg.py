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
from heapq import heappush, heappop


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

    # meetings.sort(key=lambda x:x[0]) # sort by their start times
    # rooms = [] # stores a minHeap of end times
    # heappush(rooms, meetings[0][1]) # get the first meeting's end time

    # for i in range(1, len(meetings)): # iterate through the meetings array starting at index 1

    #     currentStartTime = meetings[i][0]
    #     currentEndTime = meetings[i][1]

    #     if rooms[0] <= currentStartTime:
    #         # get the top of the pq (minHeap) and compare it to the current meeting's start time
    #         # if the current start time is greater than or equal to the previous end time
    #         heappop(rooms) # remove that meeting from the heapq
    #     heappush(rooms, currentEndTime) # push the current meeting's end time to the heap

    # return len(rooms) # return the size the minHeap, which gives us the total rooms needed throughout the day

    rooms = 0  # always be one after this point
    start_times = sorted([times[0] for times in meetings])  # O(n^2 log n)
    end_times = sorted([times[1] for times in meetings])

    length = len(meetings)

    start_ptr, end_ptr = 0, 0

    while start_ptr < length:

        # another while loop does not work.
        if start_times[start_ptr] >= end_times[end_ptr]:
            rooms -= 1
            end_ptr += 1

        rooms += 1
        start_ptr += 1

    return rooms


if __name__ == "__main__":
    # test cases here
    input1 = [(7, 10), (12, 14)]  # -> 1
    input3 = [(7, 10), (12, 14), (5, 15)]  # -> 2
    input2 = [(7, 10), (12, 14), (5, 15), (13, 14), (16, 18), (20, 21)]  # -> 3
    print(how_many_meeting_rooms(input1))
    print(how_many_meeting_rooms(input2))
    print(how_many_meeting_rooms(input3))
