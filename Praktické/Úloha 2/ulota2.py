def getEdges(input, numberOfNodes):
    edges = {i:[] for i in range(numberOfNodes)}

    for i in range(1, len(input)):
        edgeInformation = input[i].split(" ")
        nodeFrom = int(edgeInformation[0]) - 1
        nodeTo = int(edgeInformation[1]) - 1
        weight = int(edgeInformation[2]) - int(edgeInformation[3])

        edges[nodeFrom].append((nodeTo, weight))

    return edges

def bellmanFord(nodes, edges, start):

    # Relaxation
    for i in range(len(nodes)):
        for edgeFrom, edgeInfo in edges.items():
            for edgeTo, weight in edgeInfo:
                if nodes[edgeFrom][0] + weight < nodes[edgeTo][0]:
                    nodes[edgeTo][0] = nodes[edgeFrom][0] + weight
                    nodes[edgeTo][1] = edgeFrom

    # Check for negative cycles (and their paths)
    path = []
    for edgeFrom, edgeInfo in edges.items():
        for edgeTo, weight in edgeInfo:
            if nodes[edgeFrom][0] + weight < nodes[edgeTo][0]:
                currentNode = edgeTo

                while nodes[currentNode][1] != -1:
                    path.append(currentNode)

                    previousNode = currentNode
                    currentNode = nodes[currentNode][1]
                    nodes[previousNode][1] = -1

    return path


input = ["4 6", "1 2 1 1", "2 3 1 1", "3 1 1 1", "2 4 1 1", "4 1 1 2", "4 1 1 1"]
numberOfNodes = int(input[0].split(" ")[0])

start = 0
edges = getEdges(input, numberOfNodes)
nodes = [[float("+inf"), -1] for _i in range(numberOfNodes)]
nodes[start] = [0, 0]

path = bellmanFord(nodes, edges, start)
print(path)
