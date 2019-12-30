"""
You must implement the nextGreaterElement() function. 
For each element ii in a list, it finds the first element to its right which is greater than i. 
For any element that such a value does not exist, the answer is -1.

Example 1:
  input:
    [4, 6, 3, 2, 8, 1]
  output:
    [6, 8, 8, 8, -1, -1]

Example 2:
  input:
    [4, 8,  14, 2,  16, 18, 9, 5]
  output:
    [8, 14, 16, 16, 18, -1, -1, -1]

Example 3:
  input:
    [13, 3, 12, 16, 15, 11, 1, 2]
  output:
    [16, 12, 16, -1, -1, -1, 2, -1]
  
Example 4:
  input:
    [4, 6, 3, 2, 8, 1, 9, 9, 9]
  output:
    [6, 8, 8, 8, 9, 9, -1, -1, -1]
"""
# brute force solution -> O(n^2) runtime
# def nextGreaterElement(lst):
#   res = []
#   for i in range(0, len(lst), 1):
#     nextGreatest = -1
#     for j in range(i+1, len(lst), 1):
#       if lst[i] < lst[j]:
#         nextGreatest = lst[j]
#         break
#     res.append(nextGreatest)
#   return res

# stack optimized solution -> O(n) runtime 
def nextGreaterElement(lst):
    result = [-1]*len(lst)
    stack = []
    for i in range(len(lst) - 1, -1, -1):
        if stack:
            while stack and stack[-1] <= lst[i]:
                stack.pop()
        if stack:
            result[i] = stack[-1]
        stack.append(lst[i])
    return result
"""
The outer for loop begins from the end of lst. 
In each iteration, the top of the stack is compared with the current element in lst. 
Whenever the current value in lst is larger than top, that value is the next greater element in the list.

The top is popped and the current element in the list is again compared with the new top of the stack in the inner while loop. This loop stops when the top of the stack is bigger than the element of the list or the stack becomes empty.

If the stack is empty, it implies that the current element in lst does not have a next greater element. Hence, its corresponding index in res would retain the value of -1.

If the stack is not empty, then the current element has a value larger than it. Hence, the top value will be assigned to the corresponding index in res.

Continuing this process, we end up with a list containing all the next greater elements for all indices of lst.

Time Complexity #
Since we make one iteration over the list of n elements, the algorithm will work in O(n). This is a significant improvement over the brute force method’s runtime complexity of O(n2).
"""
