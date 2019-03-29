import networkx
from random import randint


def create_empty_graph(size):
    empty_graph = networkx.Graph()
    for i in range(0, size):
        empty_graph.add_node(i)
    return empty_graph


def add_edges_from_file(filename, graph):
    graph_file = open(filename, "r")
    graph_edges = graph_file.read().split()
    for i in range(0, graph.number_of_nodes()):
        for j in range(0, graph.number_of_nodes()):
            if graph_edges[graph.number_of_nodes() * i + j] != "0":
                graph.add_edge(i, j, probability=int(graph_edges[graph.number_of_nodes() * i + j]))


def add_random_edge(graph, prob):
    i = randint(0, graph.number_of_nodes() - 1)
    j = randint(0, graph.number_of_nodes() - 1)
    if graph.has_edge(i, j):
        add_random_edge(graph, prob)
    graph.add_edge(i, j, probability=prob)


def graph_reliability(graph_to_check, repeats):
    fails = 0
    for i in range(0, repeats):
        copied_graph = graph_to_check.copy()
        edges_to_remove = []
        for edge in copied_graph.edges:
            rand = randint(1, 100)
            if rand > copied_graph.get_edge_data(edge[0], edge[1])["probability"]:
                edges_to_remove.append((edge[0], edge[1]))
        for edge in edges_to_remove:
            copied_graph.remove_edge(edge[0], edge[1])
        if not networkx.is_connected(copied_graph):
            fails += 1
    return 1 - fails / repeats


if __name__ == "__main__":
    graph = create_empty_graph(20)
    add_edges_from_file("graph3", graph)
    for i in range(0, 4):
        add_random_edge(graph, 40)
    print(graph_reliability(graph, 100000))

