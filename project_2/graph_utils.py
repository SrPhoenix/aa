import networkx as nx
from networkx import Graph
import matplotlib.pyplot as plt
import numpy as np
import math
import json
import os


def generate_vertices_edges(n_vertices, percentage):
    # Generate a random graph with n vertices and n * (p/100) edges.
    # Return the list of vertices and the list of edges.

    nMec = 98515
    np.random.seed(nMec)
    max_edges = math.floor((n_vertices * (n_vertices-1)/2)  * percentage / 100)
    radius= 7

    vertices = []
    while len(vertices) < n_vertices:
        x = np.random.randint(1, 101)
        y = np.random.randint(1, 101)
        for (Vx,Vy) in vertices:
            if (Vx - x)**2 + (Vy - y)**2 < radius**2:
                break
        else:
            vertices.append((x, y))

    edges = []
    while len(edges) < max_edges:
        vertice1 = np.random.randint(0, n_vertices)
        vertice2 = np.random.randint(0, n_vertices)

        if vertice1 != vertice2 and (vertices[vertice1], vertices[vertice2]) not in edges and (vertices[vertice2], vertices[vertice1]) not in edges:
            edge = (vertices[vertice1], vertices[vertice2])
            edges.append(edge)

    return vertices, edges



def draw_graph(vertices, edges):
    # Draw a graph.
    # Return the graph.

    graph = nx.Graph()

    vertices_ids = [i for i in range(len(vertices))]
    edges_ids = [(i, j) for i in vertices_ids for j in vertices_ids if (vertices[i], vertices[j]) in edges]

    graph.add_nodes_from(vertices_ids)
    graph.add_edges_from(edges_ids)

    # positions = {i: vertices[i] for i in vertices_ids}
    # nx.draw(graph, node_color='orange', edge_color='red', with_labels=True, pos=positions)
    # plt.show()

    return graph

def remove_vertices_without_edges(graph: Graph):
    return graph.subgraph([v for v in graph if graph.degree(v) > 0])

def load_graphs():
    # return the graphs from the json files in the graph folder

    global v
    graphs = []

    n_graphs = 384

    for i in range(n_graphs):
        with open("graphs/graph_{}.json".format(i), "r") as f:
            graph_data = json.loads(f.read())

            graphs.append(nx.node_link_graph(graph_data))

    return graphs


def load_SW_graphs():

    folder_path = "SW_ALGUNS_GRAFOS"
    graphs_files = [f for f in os.listdir(folder_path) if os.path.isfile( os.path.join(folder_path, f)) ]
    # graphs_files = ["SWmediumG.txt"]
    graphs = []
    for file in graphs_files[::-1]:
        with open(folder_path + "/" + file, "r") as f:
            lines = f.readlines()
            if lines[0][0] != "0" or lines[1][0] != "0":
                continue
            print(file)
            edges = []
            vertices = lines[3]
            for line in lines[4:]:
                edge = line.strip().split(" ")
                edge_clean = [int(edge[0]), int(edge[1])]
                edges.append(edge_clean)

            G = nx.Graph()
            for vertex in range(int(vertices)):
                G.add_node(str(vertex))

            for edge in edges:
                G.add_edge(str(edge[0]),str(edge[1]))
            graphs.append(G)

    return graphs

