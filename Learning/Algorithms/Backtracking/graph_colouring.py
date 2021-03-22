# we have given three colours, problem is we have to colour in such a way that
# no two neighbouring vertices has the same colour
# m-colouring decision prob: if a graph can be coloured or not
# m-colouring optimization prob: min number of colours required such that no adjacent colours same
def isValid(adj_list, colours, vertex, colour):
    for node in adj_list[vertex]:
        if colours[node - 1] == colour:
            return False
    return True


def graphColouring(V, m, adj_list, colours, vertex):
    if vertex == V + 1:
        return True

    for colour in range(1, m + 1):
        if isValid(adj_list, colours, vertex, colour):
            colours[vertex - 1] = colour

            if graphColouring(V, m, adj_list, colours, vertex + 1):
                print(colours)

            colours[vertex - 1] = 0


adj_list = {
    1: [2, 3, 4],
    2: [1, 3],
    3: [1, 2, 4],
    4: [1, 3]
}

print(graphColouring(4, 3, adj_list, [0] * 4, 1))
