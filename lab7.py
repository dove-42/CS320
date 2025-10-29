import edgegraph


def validInput(graph, start):
    return graph is None or start is None


def get_adjacent_vertices(graph, explored_vertices, vertices):
    adjacent_vertices = []
    for vertex in vertices:
        incident_edges = graph.incident(vertex)
        for edge in incident_edges:
            curr_vertex = edge.head()
            if curr_vertex not in explored_vertices:
                explored_vertices[curr_vertex] = True
                adjacent_vertices.append(curr_vertex)
    return adjacent_vertices


def bfs(graph, start):
    if not validInput(graph, start):
        raise ValueError("Invalid graph or vertex")

    if start not in graph.vertices():
        return []

    explored_vertices = {start: True}
    lot = [(start,)]

    i = 0
    while i < len(lot):
        adjacent_vertices = get_adjacent_vertices(graph, explored_vertices, lot[i])

        if adjacent_vertices:
            lot.append(tuple(adjacent_vertices))
        i += 1

    return lot
