def getEdges(input, numberOfNodes):
    """Creates the edge dictionary"""
    edges = {i:[] for i in range(numberOfNodes)}

    for i in range(1, len(input)):
        edgeInformation = input[i].split(" ")
        u = int(edgeInformation[0]) - 1
        v = int(edgeInformation[1]) - 1
        weight = int(edgeInformation[2]) - int(edgeInformation[3])

        # (destination node, weight, "id")
        edges[u].append([v, weight, i])

    return edges

def bellmanFord(nodes, edges, start):
    """Finds the shortest path to all of the nodes using bellman-ford."""
    # Relaxation
    for i in range(len(nodes)):
        for u, edgeInfo in edges.items():
            for v, weight, id in edgeInfo:
                if nodes[u][0] + weight < nodes[v][0]:
                    nodes[v][0] = nodes[u][0] + weight
                    nodes[v][1] = u     # Save where did we come from
                    nodes[v][2] = id    # Save the ID of where we came from

    # Check for negative cycle
    path = []
    for u, edgeInfo in edges.items():
        for v, weight, id in edgeInfo:
            if nodes[u][0] + weight < nodes[v][0]:
                # Travel through the negative cycle
                currentNode = v
                while nodes[currentNode][1] != -1:
                    path.append(nodes[currentNode][2])

                    previousNode = currentNode
                    currentNode = nodes[currentNode][1]
                    nodes[previousNode][1] = -1

    return list(reversed(path))

# The input
input = ["4 6", "1 2 1 1", "2 3 1 1", "3 1 1 1", "2 4 1 1", "4 1 1 2", "4 1 1 1"]
numberOfNodes = int(input[0].split(" ")[0])

edges = getEdges(input, numberOfNodes)

# Nodes is the array containing the results of bellman-ford
nodes = [[float("+inf"), -1, -1] for _i in range(numberOfNodes)]
nodes[0] = [0, 0, 0]

# TODO: Make it so that when all nodes aren't explored, call bellman-ford again
# TODO: Call it again with weights reversed to find "positive" cycles
path = bellmanFord(nodes, edges, 0)
print(path)
