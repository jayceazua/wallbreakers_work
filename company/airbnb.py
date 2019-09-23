def get_edges(lines):
    '''given lines in correct format, return the edges it would need to form a digraph'''
    # create an array to store our edges
    edge_list = []
    # use a flag to skip the first line
    first_line_skipped = False
    # iterate through the lines in lines
    for line in lines.split('\n'):
        # check if we've skipped the first line yet
        if not first_line_skipped:
            # if not, skip this line
            first_line_skipped = True
            continue
        # set parent to None, this will store the first letter of the line
        parent = None
        # iterate through the letters in the line
        for letter in line.split(','):
            # check if the parent is none
            if parent is None:
                # if it is, we haven't seen a parent yet
                # so well set it to the current letter
                parent = letter
            # otherwise
            else:
                # add the letter, parent to our edge list
                # this means the letter points to the parent
                edge_list.append((letter, parent))
    # once we've gone through all the lines we can
    return edge_list


def build_graph(list_of_edges):
    '''given a list of edges, return a directed graph (dictionary of key, lists pairs)'''
    # use a dictionary to store our graph
    graph = {}
    # for vert1 and vert2 in our list of edges
    for vert1, vert2 in list_of_edges:
        # check if we added vert1 to the graph yet
        if vert1 in graph:
            # if so add vert2 to its list of children
            graph[vert1].append(vert2)
        # otherwise
        else:
            # add it to the graph with its value being an array of vert2
            graph[vert1] = [vert2]
        # check if vert2 is not in the graph
        if vert2 not in graph:
            # if it isn't add it to the graph with an empty arr as its val
            graph[vert2] = []
    # once we've added all the edges to our graph we can return it
    return graph


def bfs_dependers(graph, start):
    '''using breadth first search find the number of other verts you can reach from a starting vert'''
    # create a set of seen vertices to make sure we don't repeat paths
    seen = {start}
    # use a queue to store verts we need to explore the neighbors of
    queue = [start]
    # While the queue is not empty (we haven't seen everything)
    while len(queue) > 0:
        # remove (dequeue) the first item of the queue
        current_vert = queue.pop(0)
        # for all the neighbors of the removed vertex
        for neighbor in graph[current_vert]:
            # make sure we haven't seen the vertex yet
            if neighbor not in seen:
                # add the neighbor to seen and the queue
                seen.add(neighbor)
                queue.append(neighbor)
    # Once weve seen everything return the length of seen
    return len(seen)


def solution(lines):
    '''given lines in correct input format, return an array of each modules num of dependencies'''
    # get the edge list from the lines inputted
    edge_list = get_edges(lines)
    # build a directional graph
    digraph = build_graph(edge_list)
    # create an array to store each vert and their weight (num of dependencies)
    module_weights = []
    # print(digraph)
    # iterate over the graph keys or vertices
    for vert in sorted(digraph.keys()):
        # find the vertex's number of dependers
        num_of_dependers = bfs_dependers(digraph, vert)
        # add the vertex and its num of dependers to the list of module weights
        module_weights.append(f"{vert},{num_of_dependers}")
    # once we've found the weights of all our vertices we can return a list of them
    return module_weights


inp = '''5
A,E,N,S
S,H,N
E,N
H
N'''
print(solution(inp))
