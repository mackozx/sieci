from network import create_empty_graph
import networkx


def add_edges_from_file(filename, graph):
    graph_file = open(filename, "r")
    graph_edges = graph_file.read().split()
    for i in range(0, graph.number_of_nodes()):
        for j in range(0, graph.number_of_nodes()):
            if graph_edges[graph.number_of_nodes() * i + j] != "0":
                graph.add_edge(i, j, c=int(graph_edges[graph.number_of_nodes() * i + j]))


def read_a(filename, i, j, size):
    file = open(filename, "r")
    splited = file.read().split()
    if int(splited[i * size + j]) == 0:
        return int(splited[j * size + i])
    return int(splited[i * size + j])


def get_shortest_paths(graph):
    paths = []
    paths.append([])
    paths.append([])
    for i in range(0, graph.number_of_nodes()):
        for j in range(0, graph.number_of_nodes()):
            if i != j:
                paths[0].append(networkx.shortest_path(graph, i, j))
                paths[1].append(read_a("graph4", i, j, graph.number_of_nodes()))
    return paths


def get_path_edges(path):
    paths_edges = []
    for i in range(1, len(path)):
        paths_edges.append([path[i - 1], path[i]])
    return paths_edges


if __name__ == "__main__":
    graph = create_empty_graph(10)
    add_edges_from_file("graph5", graph)
    paths = get_shortest_paths(graph)
    graph_attr = []
    graph_attr.append([])
    graph_attr.append([])
    graph_attr.append([])
    for i in range(0, len(paths[0])):
        pe = get_path_edges(paths[0][i])
        for e in pe:
            print(str(e) + " " + str(paths[1][i]) + " " + str(graph.get_edge_data(e[0], e[1])["c"]))
            graph_attr[0].append(e)
            graph_attr[1].append(paths[1][i])
            graph_attr[2].append(graph.get_edge_data(e[0], e[1])["c"])
    edge_e
    for i in range(0, graph.number_of_nodes()):
        for j in range(0, graph.number_of_nodes()):
