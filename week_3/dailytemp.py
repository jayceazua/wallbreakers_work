"""
Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

Input
The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].

Sample
Input#1
T = [73, 74, 75, 71, 69, 72, 76, 73]
Output#1
[1, 1, 4, 2, 1, 1, 0, 0]

"""
from collections import deque


def dailyTemperatures(dailyTemps):

  # list of days to wait -> result same size of dailyTemps
  result = [0] * len(dailyTemps)
  # create a stack
  stack = deque() # 2 3 4 5 
  # loop over dailyTemps by index
  for index, current_temp in enumerate(dailyTemps):
    # while there's something in the stack and current temp is < top of stack
    while len(stack) > 0 and current_temp > dailyTemps[stack[-1]]:
      # this is a hotter day
      index_last_hot_temp = stack.pop()  # pop last temp
      # mark the same index in the list as the popped element as
      # offset between this index and the last hot day
      result[index_last_hot_temp] = index - index_last_hot_temp
    # add it to the stack
    stack.append(index)
  # return the answer array
  return result
