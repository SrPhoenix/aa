from graph_utils import *
import time


operations_counter = 0


def is_edge_dominating_set(graph, candidate_set):
    global operations_counter
    for edge in graph.edges():
        operations_counter+=1                     # +1 operations of comparison ( else ) 
        for dominat_edge in candidate_set:
            operations_counter += 1             # +1 operations of comparison ( graph.has_edge(node,dominat_node) ) 
            if edge in graph.edges(dominat_edge):
                break
        else:
            return False
    return True


def combinations(lst, r):
    global operations_counter
    if r == 0:
        return [[]]
    if not lst:
        return []
    operations_counter+= 2                                                                          # +2 operations of comparison ( else ) + 2 list concatenation 
    return combinations(lst[1:], r) + [item + [lst[0]] for item in combinations(lst[1:], r - 1)]    #+ 2 list concatenation

def find_minimum_edge_dominating_set(graph):
    global operations_counter
    n = len(graph.edges())+1
    min_set_size = n
    min_edge_dominating_set = set()

    for r in range(1, n):
        for candidate_set in combinations(list(graph.edges()), r):
            operations_counter+=1               # +1 operations of comparison ( is_edge_dominating_set ) 
            if is_edge_dominating_set(graph, candidate_set):
                operations_counter+=2           # +1 operations of comparison ( len(candidate_set) < min_set_size ) 
                if len(candidate_set) < min_set_size:
                    min_set_size = len(candidate_set)
                    min_edge_dominating_set = set(candidate_set)

    return min_edge_dominating_set

if __name__ == '__main__':

    graphs = load_graphs()
    results_file = open("results/ExhaustSearchGPT.txt", "w")
    csv_file = open("report/ExhaustSearchGPT.csv", "w")
    results_file.write(f"{'N Nodes':<12} {'Vertices':<12} {'Edges':<10} {'Operations':<15} {'Time':<13} {'Dominant Set'}\n")
    csv_file.write("N Nodes,Vertices,Edges,Operations,Time\n")
    print(f"{'N Nodes':<12} {'Vertices':<12} {'Edges':<10} {'Operations':<15} {'Time':<13} {'Dominant Set'}\n")
    for graph in graphs:

        n_vertices = len(graph.nodes)
        n_edges = len(graph.edges())

        start = time.time()
        dominating_set = find_minimum_edge_dominating_set(graph)
        end = time.time()
 
        print(f"{len(graph.nodes):<12} {n_vertices:<12} {n_edges:<10} {operations_counter:<15} {end - start:.4f}        {str(dominating_set)}\n")
        results_file.write(f"{len(graph.nodes):<12} {n_vertices:<12} {n_edges:<10} {operations_counter:<15} {end - start:.4f}        {str(dominating_set)}\n")
        csv_file.write(f"{len(graph.nodes)},{n_vertices},{n_edges},{operations_counter},{end - start:.4f}\n")

        # vertices = graph.subgraph([v for v in graph])
        # nodePos = nx.circular_layout(graph)

        # nx.draw(graph, node_color='orange', edge_color='red', with_labels=True,pos=nodePos)
        # plt.show()

    results_file.close()
    csv_file.close()
