from linked_list import LinkedList
from queue import Queue


class Graph:
    def __init__(self, vertices):
        # Total number of vertices
        self.vertices = vertices
        # Defining a list which can hold multiple LinkedLists equal to the number of vertices in the graph
        self.array = []
        # Creating a new LinkedList for each vertex/index of the list
        for vertex in range(vertices):
            temp = LinkedList()
            self.array.append(temp)

    def add_edge(self, source, destination):
        # As we are implementing a directed graph, (1,0) is not equal to (0,1)
        self.array[source].insert_at_head(destination)
        # If we were to implement an Undirected Graph i.e (1,0) == (0,1)
        # We would create an edge from destination towards source as well
        # i.e self.list[destination].insert_at_head(source)

    def print_graph(self):
        print(">>Adjacency List of Directed Graph<<")
        for i in range(self.vertices):
            print("|", i, end=" | => ")
            temp = self.array[i].head
            while(temp != None):
                print("[", temp.data, end=" ] -> ")
                temp = temp.next
            print("None")

    def bfs_traversal(self, source):
        """
        Time complexity: O(V + E)
        """
        result = []
        num_vertices = self.vertices
        visited = [False] * num_vertices

        q = []
        q.append(source)
        visited[source] = True

        while q:
            current_node = q.pop(0)
            result.append(str(current_node))
            current_node = self.array[current_node].head

            # linked list traversal adding it to the queue
            while current_node:
                if not visited[current_node.data]:
                    q.append(current_node.data)
                    visited[current_node.data] = True
                # go to the next node
                current_node = current_node.next
        return "".join(result)  # O(n)

    def dfs_traversal(self, source):
        """
        Time complexity: O(V + E)
        """
        result = []
        num_vertices = self.vertices
        visited = [False] * num_vertices
        s = []
        s.append(source)
        visited[source] = True

        while s:
            current_node = s.pop()
            result.append(str(current_node))
            current_node = self.array[current_node].head

            while current_node:
                if not visited[current_node.data]:
                    s.append(current_node.data)
                    visited[current_node.data] = True
                current_node = current_node.next
        return "".join(result)

    def detect_cycle(self):
        # keeps track of all the vertices that have been visited
        visited = [False]*self.vertices
        # nodes in the current recursive call
        current_visited = [False]*self.vertices
        for vertex in range(self.vertices):
            # perform a DFS
            if self._detect_cycle_rec(vertex, visited, current_visited):
                return True

        return False

    def _detect_cycle_rec(self, vertex, visited, current_visited):
        if current_visited[vertex]:  # cycle has been found
            return True

        if visited[vertex]:  # it has been visited before
            return False

        visited[vertex] = True  # mark as visited
        current_visited[vertex] = True  # add to recursion stack
        head_vertex = self.array[vertex].head
        while head_vertex:
            adjacent = head_vertex.data
            if self._detect_cycle_rec(adjacent, visited, current_visited):
                return True  # cycle is found
            head_vertex = head_vertex.next
        # remove the node from the recursive stack
        current_visited[vertex] = False
        return False


if __name__ == "__main__":
    g1 = Graph(4)
    g1.add_edge(0, 1)
    g1.add_edge(1, 2)
    g1.add_edge(1, 3)
    g1.add_edge(3, 0)
    g2 = Graph(3)
    g2.add_edge(0, 1)
    g2.add_edge(1, 2)

    print(g1.detect_cycle())
    print(g2.detect_cycle())
