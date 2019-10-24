"""
A queue is an abstract data type that maintains the order in which elements were added to it, allowing the oldest elements to be removed from the front and new elements to be added to the rear. This is called a First-In-First-Out (FIFO) data structure because the first element added to the queue (i.e., the one that has been waiting the longest) is always the first one to be removed.

A basic queue has the following operations:

Enqueue: add a new element to the end of the queue.
Dequeue: remove the element from the front of the queue and return it.
In this challenge, you must first implement a queue using two stacks. Then process  queries, where each query is one of the following  types:

1 x: Enqueue element  into the end of the queue.
2: Dequeue the element at the front of the queue.
3: Print the element at the front of the queue.
Input Format

The first line contains a single integer, , denoting the number of queries.
Each line  of the  subsequent lines contains a single query in the form described in the problem statement above. All three queries start with an integer denoting the query , but only query  is followed by an additional space-separated value, , denoting the value to be enqueued.

Constraints

It is guaranteed that a valid answer always exists for each query of type .
Output Format

For each query of type , print the value of the element at the front of the queue on a new line.

Sample Input

10
1 42
2
1 14
3
1 28
3
1 60
1 78
2
2
Sample Output

14
14
Explanation

We perform the following sequence of actions:

Enqueue ; .
Dequeue the value at the head of the queue, ; .
Enqueue ; .
Print the value at the head of the queue, ; .
Enqueue ; .
Print the value at the head of the queue, ; .
Enqueue ; .
Enqueue ; .
Dequeue the value at the head of the queue, ; .
Dequeue the value at the head of the queue, ; .
"""


import os
# 1 x: Enqueue element  into the end of the queue.

# 2: Dequeue the element at the front of the queue.

# 3: Print the element at the front of the queue.


class Queue:

  def __init__(self):
    self.stack_one = []
    self.stack_two = []
    self.answers = []

  def enqueue(self, val):
    self.stack_one.append(val)

  def dequeue(self):
    # check that the second stack is empty and that stack one only has one item.
    if self._is_empty(self.stack_two) and self._stack_length(self.stack_one) == 1:
      self.stack_one.pop()

    # check is the second stack is empty and check if the first stack greater than one
    elif self._is_empty(self.stack_two) and self._stack_length(self.stack_one) > 1:
      self._shift_stacks(self.stack_one, self.stack_two)
      self.stack_two.pop()

    # check if the second stack is not empty
    elif not self._is_empty(self.stack_two):
      self.stack_two.pop()

  def peek(self):
    # check that the second stack is empty and that stack one only has one item.
    if self._is_empty(self.stack_two) and self._stack_length(self.stack_one) == 1:
      self.answers.append(self.stack_one[0])

    # check is the second stack is empty and check if the first stack greater than one
    elif self._is_empty(self.stack_two) and self._stack_length(self.stack_one) > 1:
      self._shift_stacks(self.stack_one, self.stack_two)
      self.answers.append(self.stack_two[-1])

    # check if the second stack is not empty
    elif not self._is_empty(self.stack_two):
      self.answers.append(self.stack_two[-1])

  # helper functions..

  def _shift_stacks(self, stack_one, stack_two):
    while not self._is_empty(stack_one):
      stack_two.append(stack_one.pop())

  def _is_empty(self, stack):
    return len(stack) == 0

  def _stack_length(self, stack):
    return len(stack)


def run_operations(query, queue):

  query = query.split(" ")

  if query[0] == '1':
    val = query[1]
    queue.enqueue(val)

  if query[0] == '2':
    queue.dequeue()

  if query[0] == '3':
    queue.peek()


if __name__ == '__main__':
    with open(os.environ['OUTPUT_PATH'], 'w') as f:

      commands = int(input())

      queue = Queue()

      while commands > 0:

        command = input()

        run_operations(command, queue)

        commands -= 1

      for answer in queue.answers:
        f.write(f"{answer}\n")
