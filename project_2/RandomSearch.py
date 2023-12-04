import networkx as nx
import random
from graph_utils import *
import time
from itertools import combinations



def is_edge_dominating_set(graph, candidate_set):
    for edge in graph.edges():
        for dominat_edge in candidate_set:
            if edge in graph.edges(dominat_edge):
                break
        else:
            return False
    return True

def min_edge_dominating_set(graph, iterations=5000, max_iterations_without_improvement=100, initial_set_size=1):
    min_dominating_set = None
    tried_solutions = set()
    solutions_tested_counter = 0
    basic_operations_counter = 0
    current_set_size = initial_set_size

    while solutions_tested_counter < iterations:
        dominating_set, basic_operations = local_search(graph.copy(), current_set_size, tried_solutions, max_iterations_without_improvement)

        basic_operations_counter += basic_operations 
        basic_operations_counter += 1
        solutions_tested_counter += 1
        if is_edge_dominating_set(graph, dominating_set):
            min_dominating_set = dominating_set
            break


    return min_dominating_set, basic_operations_counter, solutions_tested_counter

def local_search(graph, set_size, tried_solutions, max_iterations_without_improvement):
    iterations_without_improvement = 0
    basic_operations = 0
    lst_comb = tuple(combinations(graph.edges(), set_size))
    solution = random.choice(lst_comb)
    # print(solution)
    # print(tried_solutions)
    while solution in tried_solutions :
        solution = random.choice(lst_comb)
        iterations_without_improvement += 1

        # print(lst_comb)
        # print(solution)
        # print(tried_solutions)
        # print(set_size)
        basic_operations += 2
        if iterations_without_improvement >= max_iterations_without_improvement or len(tried_solutions) ==  len(lst_comb):
            set_size += 1
            lst_comb = tuple(combinations(graph.edges(), set_size))
            iterations_without_improvement = 0
 

    basic_operations += 1
    tried_solutions.add(solution)
    if set_size == 1:
        solution = solution[0]   
    return solution , basic_operations

def run( graphs ,path ):
    results_file = open("results/"+path+".txt", "w")
    csv_file = open("results/"+path+".csv", "w")
    results_file.write(f"{'N Nodes':<12} {'Vertices':<12} {'Edges':<10} {'Attemps':<15} {'Operations':<15} {'Time':<13} {'Dominant Set'}\n")
    csv_file.write("N Nodes,Vertices,Edges,Attemps,Operations,Time\n")
    print(f"{'N Nodes':<12} {'Vertices':<12} {'Edges':<10} {'Attemps':<15}{'Operations':<15} {'Time':<13} {'Dominant Set'}\n")
    for graph in graphs:

        n_vertices = len(graph.nodes)
        n_edges = len(graph.edges())




        start = time.time()
        min_dominating_set, basic_operations_counter, solutions_tested_counter = min_edge_dominating_set(graph)
        end = time.time()
 
        print(f"{len(graph.nodes):<12} {n_vertices:<12} {n_edges:<10} {solutions_tested_counter:<15} {basic_operations_counter:<15} {end - start:.4f}        {str(min_dominating_set)}\n")
        results_file.write(f"{len(graph.nodes):<12} {n_vertices:<12} {n_edges:<10} {solutions_tested_counter:<15} {basic_operations_counter:<15} {end - start:.4f}        {str(min_dominating_set)}\n")
        csv_file.write(f"{len(graph.nodes)},{n_vertices},{n_edges},{basic_operations_counter},{solutions_tested_counter},{end - start:.4f}\n")
        # vertices = graph.subgraph([v for v in graph])
        # nodePos = nx.circular_layout(graph)

        # nx.draw(graph, node_color='orange', edge_color='red', with_labels=True,pos=nodePos)
        # plt.show()

    results_file.close()
    csv_file.close()

if __name__ == '__main__':

    # graphs = load_graphs()
    # run(graphs, "RandomSearch")
    graphsSW = load_SW_graphs()
    run(graphsSW, "RandomSearchSW")
    
