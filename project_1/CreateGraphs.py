from graph_utils import *

def CreateGraphs(v=100):
    graph_id = 0

    for n_vertices in range(5, v+1):

        for percentage in [12.5, 25, 50, 75]:
            vertices, edges = generate_vertices_edges(n_vertices, percentage)

            print("---")
            print("Number of vertices:", len(vertices))
            print("Number of edges:", len(edges))

            print("Vertices:", vertices)
            print("Edges:", edges)

            graph = draw_graph(vertices, edges)
            graph_data = nx.node_link_data(graph)
            print(graph_data)
            # with open("graphs/graph_{}.json".format(graph_id), "w") as f:
            #     f.write(json.dumps(graph_data))

            graph_id += 1
        break

if __name__ == '__main__':
    CreateGraphs()