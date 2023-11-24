import heapq

class Graph:
    def __init__(self):
        self.vertices = []
        self.edges = {}

    def read_graph(self):
        f = open("../files/small_graph.txt", "r")

        no_vert = int(f.readline())
        for i in range(1, no_vert + 1):
            self.vertices.append(str(i))
        while True:
            line = f.readline()
            if not line:
                break
            if len(line) > 1:
                edge, cost = line.split(" ")
                v1,v2 = edge.split(",")
                self.add_edge(v1,v2,int(cost))

    def isVert(self,v):
        if v not in self.vertices:
            return False
        return True

    def add_edge(self, source, destination, cost):
        self.edges[(source, destination)] = cost
        self.edges[(destination, source)] = cost

    def prim(self, start_vertex):
        visited = set()
        spanning_tree = []
        heap = []

        visited.add(start_vertex)
        for neighbor in self.get_neighbors(start_vertex):
            heapq.heappush(heap, (self.edges[(start_vertex, neighbor)], start_vertex, neighbor))

        while heap:
            cost, source, destination = heapq.heappop(heap)

            if destination not in visited:
                visited.add(destination)
                spanning_tree.append((source, destination))

                for neighbor in self.get_neighbors(destination):
                    if neighbor not in visited:
                        heapq.heappush(heap, (self.edges[(destination, neighbor)], destination, neighbor))

        cost = 0
        for edge in spanning_tree:
            cost += int(self.edges[edge])

        self.write_to_file(spanning_tree)

        return spanning_tree, cost

    def get_neighbors(self, vertex):
        neighbors = []
        for (source, destination), _ in self.edges.items():
            if source == vertex and destination not in neighbors:
                neighbors.append(destination)
            elif destination == vertex and source not in neighbors:
                neighbors.append(source)
        return neighbors

    def write_to_file(self,spanning_tree: list):
        f = open("../files/last_spanning_tree.txt", "w")
        f.write(self.mst_to_string(spanning_tree))
        f.close()

    def write_all(self):
        rs = ""
        f = open("../files/last_spanning_tree.txt", "w")
        for v in self.vertices:
            mst, cst = self.prim(v)
            f.write(self.mst_to_string(mst))
            rs += f"Cost: {cst}\n{self.mst_to_string(mst)}"
        f.close()

        return rs

    def mst_to_string(self, spanning_tree):
        rs = ""
        rs += str(len(self.vertices)) + "\n"
        for edge in spanning_tree:
            rs += f"{edge[0]},{edge[1]} {self.edges[edge]}\n"
            pass
        return rs

gr = Graph()
gr.read_graph()