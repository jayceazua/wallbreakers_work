"""
Given a reference of a node in a connected undirected graph, 
return a deep copy (clone) of the graph. Each node in the graph 
contains a val (int) and a list (List[Node]) of its neighbors.

 

Example:



Input:
{"$id":"1","neighbors":[{"$id":"2","neighbors":[{"$ref":"1"},
{"$id":"3","neighbors":[{"$ref":"2"},{"$id":"4","neighbors":[{"$ref":"3"},{"$ref":"1"}],"val":4}],"val":3}],"val":2},{"$ref":"4"}],"val":1}

Explanation:
Node 1's value is 1, and it has two neighbors: Node 2 and 4.
Node 2's value is 2, and it has two neighbors: Node 1 and 3.
Node 3's value is 3, and it has two neighbors: Node 2 and 4.
Node 4's value is 4, and it has two neighbors: Node 1 and 3.
 

Note:

The number of nodes will be between 1 and 100.
The undirected graph is a simple graph, which means no repeated edges and no self-loops in the graph.
Since the graph is undirected, if node p has node q as neighbor, then node q must have node p as neighbor too.
You must return the copy of the given node as a reference to the cloned graph.
"""

from copy import deepcopy
# python has a built-in deepcopy function


class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors


def cloneGraph(node):
    if not node:
        return node

    stack = [node]
    visited = {}
    visited[node] = Node(node.val, [])

    while stack:  # Depth-first search
        current_node = stack.pop()

        for neighbor in current_node.neighbors:  # get all the neighbors of the current node
            if neighbor not in visited:  # check if the neighbor node has been visited before
                # create a new node with with the neighbor's value
                visited[neighbor] = Node(neighbor.val, [])
                # add to stack
                # append that neighbor into the stack to later get their neighbors
                stack.append(neighbor)
            # from the new node created append it to the current node's neighbor list
            visited[current_node].neighbors.append(visited[neighbor])
    return visited[node]
