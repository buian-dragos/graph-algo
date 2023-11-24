class Graph:
    def __init__(self):
        self._outEdges = {}
        # for i in range(n):
        #     self._outEdges[i] = []

    def add_node(self,ind: int):
        if ind in self._outEdges.keys():
            return False
        self._outEdges[ind] = []

    def add_edge(self, x, y):
        self.add_node(x)
        self.add_node(y)
        if y in self._outEdges[x]:
            return False
        self._outEdges[x].append(y)
        self._outEdges[y].append(x)
        # print(self._outEdges)
        return True

    def parseX(self):
        return range(len(self._outEdges))

    def parseNOut(self, x):
        return list(self._outEdges[x])

    def parseNIn(self, x):
        inEdges = []
        for i in self.parseX():
            if x in self._outEdges[i]:
                inEdges.append(i)
        return inEdges

    def isEdge(self, x, y):
        return y in self._outEdges[x]

    def __str__(self):
        rs = ""
        for x in self._outEdges.keys():
            rs += str(x) + " ->"
            for y in self._outEdges[x]:
                rs += " " + str(y)
            rs += "\n"
        return rs


# the function that was already given
# returns the vertices that are accessible from vertex 's' in graph 'g'
def accessible(g, s):
    acc = set()
    acc.add(s)
    list = [s]
    while len(list) > 0:
        x = list[0]
        list = list[1 : ]
        for y in g.parseNOut(x):
            if y not in acc:
                acc.add(y)
                list.append(y)
    return acc


# creates the first graph
# 5 vertices and 8 edges
# 1 component
def graph1():
    gr = Graph()
    gr.add_edge(0,1)
    gr.add_edge(1,2)
    gr.add_edge(2,3)
    gr.add_edge(3,4)
    gr.add_edge(0,2)
    gr.add_edge(0,4)
    gr.add_edge(1,4)
    gr.add_edge(1,3)

    return gr


# creates the 2nd graph
# 10 vertices and 8 edges
# 3 components (1 isolated - "0")
def graph2():
    gr = Graph()

    gr.add_node(0)

    gr.add_edge(1,2)
    gr.add_edge(1,4)
    gr.add_edge(2,4)
    gr.add_edge(2,3)

    gr.add_edge(5,6)
    gr.add_edge(7,8)
    gr.add_edge(7,9)
    gr.add_edge(5,9)

    return gr


# checks if a vertex    X was already visited
def in_visited(i,vis):
    for v in vis:
        if i in v:
            return True
    return False

# creates a list with the connected components as generated graph objects
def generate_graph_list(visited):
    graph_list = []
    for vis in visited:
        temp = Graph()
        if len(vis) == 1:
            temp.add_node(vis.pop())
        else:
            for x in vis:
                for y in gr.parseNOut(x):
                    temp.add_edge(x, y)
        print(temp)
        graph_list.append(temp)
    return graph_list

if __name__ == '__main__':
    inp = input("Choose a graph: ")
    if inp == "1":
        gr = graph1()
    elif inp == "2":
        gr = graph2()
    else:
        print("Choose something else")
        exit()
    visited = []
    for i in gr.parseX():
        if not in_visited(i,visited):
            visited.append(accessible(gr,i))
    print(f"Number of connected components: {len(visited)}\n")
    print("Connected components: ")
    for vis in visited:
        print(vis)
    graph_list = generate_graph_list(visited)

    print("List with graph elements: ")
    print(graph_list)
    print()
    print("Edges for each graph: ")

    i = 1
    for graph in graph_list:
        print(f"Graph {i}:")
        i += 1
        print(graph)


