"""
Meeting rooms

Given an array of meeting time intervals consisting of start and end times
[[s1, e1], [s2, e2]...] (s < e) determine if a person could attend all meetings.
"""


class Interval:
    def __init__(self):
        self.start = 0
        self.end = 0


def canAttendMeetings(intervals):
    starts = [0]*len(intervals)
    ends = [0]*len(intervals)

    # populate both then sort them
    for i, interval in enumerate(intervals):  # O(n)
        start[i] = interval.start
        end[i] = interval.end
    # O(n log n) and this is done in-place
    starts.sort()
    ends.sort()
    # check for any overlap
    for i in range(len(starts) - 1):
        if starts[i + 1] < ends[i]:
            return False
    return True
