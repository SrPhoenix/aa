from graph_utils import *
import time

def greedy_edge_dominating_set(graph):

    operations_counter = 0
    attempts_counter = 0

    # Initialize an empty set to store the selected edges
    dominating_set = set()

    # Create a copy of the graph to work with
    remaining_edges = set(graph.edges())

    # While there are remaining edges, select an edge that covers a new vertex
    while remaining_edges:
        best_edge = list(remaining_edges)[0]
        max_neighbors = 0
        
        # Iterate over the remaining edges and find the edge that covers the most new vertices
        for edge in remaining_edges:
            e_neighbors = len(set(graph.edges(edge)) - dominating_set)          
            attempts_counter += 1                
            if e_neighbors > max_neighbors:                                             
                best_edge = edge
                max_neighbors = e_neighbors

        # Add the best edge to the dominating set and remove covered vertices and edges
        operations_counter += 1                
        dominating_set.add(best_edge)


        remaining_edges.discard(tuple(sorted(tuple(best_edge))))
        for edge in graph.edges(best_edge):
            remaining_edges.discard(tuple(sorted(tuple(edge))))

    return operations_counter, attempts_counter, dominating_set



if __name__ == '__main__':

    graphs = load_graphs()
    results_file = open("results/GreedySearch.txt", "w")
    csv_file = open("report/GreedySearch.csv", "w")
    results_file.write(f"{'N Nodes':<12} {'Vertices':<12} {'Edges':<10} {'Attemps':<15} {'Operations':<15} {'Time':<13} {'Dominant Set'}\n")
    csv_file.write("N Nodes,Vertices,Edges,Attemps,Operations,Time\n")
    print(f"{'N Nodes':<12} {'Vertices':<12} {'Edges':<10} {'Attemps':<15}{'Operations':<15} {'Time':<13} {'Dominant Set'}\n")
    for graph in graphs:

        n_vertices = len(graph.nodes)
        n_edges = len(graph.edges())


        start = time.time()
        operations_counter,  attempts_counter, dominating_set = greedy_edge_dominating_set(graph)
        end = time.time()




        print(f"{len(graph.nodes):<12} {n_vertices:<12} {n_edges:<10} {attempts_counter:<15} {operations_counter:<15} {end - start:.4f}        {str(dominating_set)}\n")
        results_file.write(f"{len(graph.nodes):<12} {n_vertices:<12} {n_edges:<10} {attempts_counter:<15} {operations_counter:<15} {end - start:.4f}        {str(dominating_set)}\n")
        csv_file.write(f"{len(graph.nodes)},{n_vertices},{n_edges},{operations_counter},{attempts_counter},{end - start:.4f}\n")

        # vertices = graph.subgraph([v for v in graph])
        # nodePos = nx.circular_layout(graph)

        # nx.draw(graph, node_color='orange', edge_color='red', with_labels=True,pos=nodePos)
        # plt.show()

    results_file.close()
    csv_file.close()



# def greedy_edge_dominating_set(graph):

#     operations_counter = 0
#     attempts_counter = 0

#     # Initialize an empty set to store the selected edges
#     dominating_set = set()

#     # Create a copy of the graph to work with
#     remaining_edges = set(graph.edges())

#     # While there are remaining edges, select an edge that covers a new vertex
#     while remaining_edges:
#         best_edge = list(remaining_edges)[0]
#         # max_neighbors = 0
#         best_covered_vertices = set()
#         # Iterate over the remaining edges and find the edge that covers the most new vertices
#         for edge in remaining_edges:
#             attempts_counter += 1
#             # e_neighbors = len(set(graph.edges(edge)) - dominating_set)           # +1 operations accour (set difference)

#             # # print(edge)
#             # # print(e_neighbors)
#             # attempts_counter+=1                                        

#             # if e_neighbors > max_neighbors:                                             # +1 operations accour (comparison)
#             #     best_edge = edge
#             #     max_neighbors = e_neighbors
#             covered_vertices = set(edge)
#             operations_counter += 1                 #Comparison below 
#             if len(covered_vertices) > len(best_covered_vertices):
#                 best_edge = edge
#                 best_covered_vertices = covered_vertices

#         operations_counter += 1                 #Add element to set
#         # Add the best edge to the dominating set and remove covered vertices and edges
#         dominating_set.add(best_edge)


#         remaining_edges.discard(tuple(sorted(tuple(best_edge))))
#         for edge in graph.edges(best_edge):
#             remaining_edges.discard(tuple(sorted(tuple(edge))))




#         operations_counter += 1                 #set difference
#     return operations_counter, attempts_counter, dominating_set

