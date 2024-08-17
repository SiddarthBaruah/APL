import sys


# read command line args to know which file to parse
lines = open(sys.argv[1], "r").readlines()

# dictionary of vertices -- this keeps track of which grouping each vertex
# goes to
vertices = {}

# dictionary of vertices to neighbours
neighbours = {}

# array of edges
edges = [] # weight, node1, node2

# unnecessary variable that we forgot to remove
i = 0

for line in lines[1:]:
    split = line.strip().split()

    # initially leave the grouping of each vertex as None
    vertices[split[0]] = None
    vertices[split[1]] = None

    for i in 0, 1:
        # add each vertex to the neighbours dictionary
        if split[i] not in neighbours:
            neighbours[split[i]] = []

        # add the neighbour and the weight of the edge
        # this adds [neighbour, weight] to the array
        neighbours[split[i]].append([split[1 - i], int(split[2])])

    # add [weight, vertex1, vertex2] to the edge array
    edges.append([int(split[2]), split[0], split[1]])

print(len(edges))

# our first idea was to go down a reverse-sorted list of edges, and keep
# splitting edges down this list until we can't split anymore

# reverse sort the edges
edges.sort()
edges.reverse()

# while cutting an edge, if both vertices happen to have a grouping of
# None, this function decides where to put the vertex on the left -- we
# wanted to eventually randomize this process so we left it as a function.
# we ended up coming up with a better strategy so we didn't implement this.
def where_to_put_new_ones():
    return 0

# sum of edges that we cut (variable name is a misnomer)
sum_vert = 0

for edge in edges:
    n1 = vertices[edge[1]]
    n2 = vertices[edge[2]]

    # we look at each edge in descending order of weight, and consider the
    # vertices that this edge connects

    # if both vertices have no grouping assigned, put them in different
    # groups based on where_to_put_new_ones

    # if one of the vertices has no group and the other does, add the one
    # that doesn't have a group in the group opposite to the one that does

    # if both vertices are already given groups, don't do anything

    if n1 is None:
        if n2 is None:
            vertices[edge[1]] = where_to_put_new_ones()
            vertices[edge[2]] = 1 - vertices[edge[1]]
        else:
            vertices[edge[1]] = 1 - vertices[edge[2]]
    elif n2 is None:
        vertices[edge[2]] = 1 - vertices[edge[1]]

    # if the vertices are in different groups, add the weight of this edge
    # to our sum
    if vertices[edge[1]] != vertices[edge[2]]:
        sum_vert += edge[0]

print(sum_vert)

# this was our first round of submissions

# we then figured out a strategy to optimize our solution
# we loop through the vertices, and judge whether swapping it to the other
# group is advantageous or not
# if we move a vertex from one group to another, the edges that are
# currently cut (we call these "active edges") will be uncut, and the ones
# that aren't cut (we call these "inactive edges") will be cut
# so we calculate the sums of active and inactive edges and compare them
# we swap groups if the inactive sum is bigger than the active sum


