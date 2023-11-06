def Dominant(box, ver) -> List[int]:
	S = [] # set S
	for i in range(ver):
		if not box[i]:
			S.append(i)
			box[i] = True
			for j in range(len(g[i])):
				if not box[g[i][j]]:
					box[g[i][j]] = True
					break
	return S


def print_results(graph, A, B, maximum_cut):

    print("---")
    print("Number of vertices:", len(graph))
    print("Number of edges:", len(graph.edges))

    # print("Vertices:", list(graph))
    # print("Edges:", list(graph.edges))

    print("A: ", A)
    print("B: ", B)
    print("Maximum cut:", maximum_cut)