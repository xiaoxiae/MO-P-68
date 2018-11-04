import sys

def constructGraph(input, numberOfNodes, specialEdges):
    """Constructs information about the graph."""

    # Construct the edge discionary skeleton
    edges = {edge:[] for edge in range(numberOfNodes)}

    # Dictionary that stores the statuses of the edges (keys are edge tuples)
    edgeStatuses = {}

    # The list of special edges
    specialEdgesList = []

    for i in range(1, len(input)):
        nodes = input[i].split(" ")

        # Nodes are order 1 to n, this will work better with arrays
        nodeFrom = min(int(nodes[0]), int(nodes[1])) - 1
        nodeTo = max(int(nodes[0]), int(nodes[1])) - 1

        # Status code for special edge is 1 and 0 for unexplored edge
        if specialEdges > 0:
            # Add the edge both ways
            edges[nodeFrom].append(nodeTo)
            edges[nodeTo].append(nodeFrom)

            # Add it as a special edge to edgeStatuses
            edgeStatuses[(nodeFrom, nodeTo)] = 1
            specialEdgesList.append((nodeFrom, nodeTo))
            specialEdges -= 1
        else:
            # Add the edge both ways
            edges[nodeFrom].append(nodeTo)
            edges[nodeTo].append(nodeFrom)

            # Add it as an untraversed edge to edgeStatuses
            edgeStatuses[(nodeFrom, nodeTo)] = 0

    return [edges, edgeStatuses, specialEdgesList]

def dfs(edges, edgeStatuses, currentNode, endNode, exploredNodes):
    """DFS seaches the edge dictionary. The status codes are as follows:
        0: untraversed
        1: special
        2: traversed
        3: special traversed
    """

    # For all of the neighbours of the current node:
    for i in range(0, len(edges[currentNode])):
        neighbour = edges[currentNode][i]
        edge = (min(currentNode, neighbour), max(currentNode, neighbour))
        status = edgeStatuses[edge]

        # Change the status of the edges
        if status == 3: # We can't traverse a traversed special edge
            continue
        elif status == 0:   # Change untraversed to traversed
            edgeStatuses[edge] = 2
            status = 2
        elif status == 2:   # Change traversed to untraversed
            edgeStatuses[edge] = 0
            status = 0
        elif status == 1:   # Change special untraversed to special traversed
            edgeStatuses[edge] = 3
            status = 3

        # If we reached the end, return True
        if neighbour == endNode:
            return True

        # If the node wasn't explored yet
        if not exploredNodes[neighbour]:
            # Explore it and go down the rabbit hole
            exploredNodes[neighbour] = True
            result = dfs(edges, edgeStatuses, neighbour, endNode, exploredNodes)

            # If we found the end, return True
            if result:
                return True

        # Roll-back the status that we just changed
        if status == 3:     # Un-traverse a special traversed edge
            edgeStatuses[edge] = 1
        elif status == 0:   # Change untraversed to traversed
            edgeStatuses[edge] = 2
        elif status == 2:   # Change traversed to untraversed
            edgeStatuses[edge] = 0

    # If this is a dead end, return False
    return False

# Read from stdin
input = []
for line in sys.stdin:
    input.append(line)

# Information about the graph
graphInfo = input[0].split(" ")
numberOfNodes = int(graphInfo[0])
numberOfSpecialEdges = int(graphInfo[2])

# Generated information about the graph
edgeInformation = constructGraph(input, numberOfNodes, numberOfSpecialEdges)
edges = edgeInformation[0]          # The dictionary of all edges
edgeStatuses = edgeInformation[1]   # The dictionary of the status of edges
specialEdges = edgeInformation[2]   # A list of all the special edges

for specialEdge in specialEdges:
    # If it's already added, ignore it
    if edgeStatuses[specialEdge] == 3:
        continue

    # Create array so dfs doesn't go in loops
    exploredNodes = [False] * numberOfNodes
    exploredNodes[specialEdge[0]] = True

    # Make the current special edge explored, so we have to find a cycle
    edgeStatuses[specialEdge] = 3


    startNode, endNode = specialEdge[0], specialEdge[1]
    result = dfs(edges, edgeStatuses, startNode, endNode, exploredNodes)

    # If it can't be added
    if not result:
        print(-1)
        quit()

# Add all of the unexplored edges to the list (we want to demolish those)
list = []
for k, v in edgeStatuses.items():
    if v == 0:
        list.append(k)

# Print the edges to demolish (and how many of them are there)
print(len(list))
for tuple in list:
    print(str(tuple[0] + 1)+" "+str(tuple[1] + 1))
