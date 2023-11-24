from random import randint as ri


class Service:
    def __init__(self,repo):
        self.repo = repo

    def add_vertex(self,v):
        if self.is_vertex(v):
            print("Vertex already exists!")
            return

        self.repo.add_vertex(v)

    def remove_vertex(self,v):
        if not self.is_vertex(v):
            print(f"{v} is not a vertex")
            return
        edges = tuple(self.repo.edges.keys())
        for edge in edges:
            if v in edge:
                del self.repo.edges[edge]

        del self.repo.dIn[v]
        del self.repo.dOut[v]

        dIn = tuple(self.repo.dIn.keys())
        for key in dIn:
            if v in self.repo.dIn[key]:
                self.repo.dIn[key].pop(self.repo.dIn[key].index(v))
            if v in self.repo.dOut[key]:
                self.repo.dOut[key].pop(self.repo.dOut[key].index(v))


    def add_edge(self,edge,value):
        if self.is_edge(edge):
            print("Edge already exists!")
            return False

        v1, v2 = edge.split(',')
        if not self.is_vertex(v1):
            self.repo.add_vertex(v1)
        if not self.is_vertex(v2):
            self.repo.add_vertex(v2)

        self.repo.update_edge(edge,value)
        self.repo.add_value_to_vertex("dIn",v2,v1)
        self.repo.add_value_to_vertex("dOut",v1,v2)

        return True

    def is_vertex(self,v):
        if self.repo.dIn.get(v,"Not a vertex") == "Not a vertex":
            return False
        else:
            return True

    def is_edge(self,edge): #edge format is now ("v1,v2")
        if self.repo.edges.get(edge,"Not an edge") == "Not an edge":
            return False
        else:
            return True

    def in_degree(self,v):
        if not self.is_vertex(v):
            return f"{v} is not a vertex"

        return len(self.repo.dIn[v])

    def out_degree(self, v):
        if not self.is_vertex(v):
            print(f"{v} is not a vertex")
            return
        return len(self.repo.dOut[v])

    def get_value_of_edge(self,edge):
        return self.repo.edges.get(edge,"Edge doesn't exist")

    def modify_value_of_edge(self,edge,value):
        if not self.is_edge(edge):
            print(f"{edge} isn't an edge")
            return
        self.repo.update_edge(edge,value)

    def iterate_inbound(self,v):
        if not self.is_vertex(v):
            print(f"{v} is not a vertex")
            return
        index = 0
        n = self.in_degree(v)
        if n == 0:
            print(f"There are no inbound edges for vertex {v}")
        while True:
            current_edge = self.repo.dIn[v][index] + ',' + v
            print(f"{current_edge} {self.repo.edges[current_edge]}")
            print("(commands: \"next\", \"back\", \"menu\"")
            command = input(">")
            if command == "next":
                if index == n - 1:
                    index = 0
                else:
                    index += 1
            elif command == "back":
                if index == 0:
                    index = n - 1
                else:
                    index -= 1
            elif command == "menu":
                return
            else:
                print("Invalid command")

    def iterate_outbound(self,v):
        if not self.is_vertex(v):
            print(f"{v} is not a vertex")
            return
        index = 0
        n = self.out_degree(v)
        if n == 0:
            print(f"There are no outbound edges for vertex {v}")
        while True:
            current_edge = v + ',' + self.repo.dOut[v][index]
            print(f"{current_edge} {self.repo.edges[current_edge]}")
            print("(commands: \"next\", \"back\", \"menu\"")
            command = input(">")
            if command == "next":
                if index == n - 1:
                    index = 0
                else:
                    index += 1
            elif command == "back":
                if index == 0:
                    index = n - 1
                else:
                    index -= 1
            elif command == "menu":
                return
            else:
                print("Invalid command")

    def iterate_vertices(self):
        vertices = tuple(self.repo.dIn.keys())
        for i in range(0,self.number_of_vertices()):
            print(vertices[i])

    def number_of_vertices(self):
        return len(self.repo.dIn)

    def number_of_edges(self):
        return len(self.repo.edges)

    def print_dictionaries(self):
        return f"dIn: {str(self.repo.dIn)}\ndOUT: {str(self.repo.dOut)}\nedges: {str(self.repo.edges)}"

    def print_edges(self):
        string = ""
        edges = self.repo.edges.keys()
        for edge in edges:
            v1, v2 = edge.split(',')
            string += f"{v1} {v2} {self.repo.edges[edge]}\n"
        return string

    def generate_random(self,no_vert,no_edges):
        for i in range(0,no_vert-1):
            self.add_vertex(str(i))

        ct = 0
        while ct < no_edges:
            v1 = str(ri(0,no_vert - 1))
            v2 = str(ri(0,no_vert - 1))
            value = str(ri(0,100))
            current_edge = f"{v1},{v2}"
            if self.add_edge(current_edge,value):
                ct += 1

    def read_file(self,file_name):
        file = open(f"../files/{file_name}", "r")
        n, m = map(int, file.readline().split())
        for _ in range(m):
            v1, v2, edge_cost = map(int, file.readline().split())
            edge = str(v1) + ',' + str(v2)
            self.add_edge(edge, str(edge_cost))
        file.close()

    def write_file(self,file_name):
        file = open(f"../files/{file_name}", "w")
        edges = self.repo.edges.keys()
        file.write(f"{self.number_of_vertices()} {self.number_of_edges()}\n")
        for edge in edges:
            v1, v2 = edge.split(',')
            file.write(f"{v1} {v2} {self.repo.edges[edge]}\n")
        file.close()