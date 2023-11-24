from prims import Graph

class Ui:
    def __init__(self):
        self.graph = Graph()

    def run(self):
        self.graph.read_graph()
        print("1. MST from a starting vertex")
        print("2. Write all MSTs")
        opt = input("Choose: ")
        if opt == "1":
            v = input("Starting vertex: ")
            if not self.graph.isVert(v):
                print("Invalid vertex")
                exit()

            spanning_tree, cost = self.graph.prim(v)

            print(f"Spanning Tree of cost {cost}:")
            for edge in spanning_tree:
                print(f"{edge[0]} - {edge[1]}")
        elif opt == "2":
            print("All the spanning trees: ")
            print(self.graph.write_all())


ui = Ui()

ui.run()