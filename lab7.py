import edgegraph


def validInput(graph, start):
    return graph is None or start is None


def bfs(graph, start):
    if not validInput(graph, start):
        raise ValueError("Invalid graph or vertex")

    if start not in graph.vertices():
        return []

    '''Useful edgegraph methods
        graph:
            graphObject.incident(vertex)'''
