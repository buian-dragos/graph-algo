class Repo:
    def __init__(self):
        self.dIn = {}
        self.dOut = {}
        self.edges = {}

    def add_vertex(self, key):
        self.dIn[key] = []
        self.dOut[key] = []

    def add_value_to_vertex(self, dict, key, value):
        if dict == "dIn":
            self.dIn[key].append(value)
        elif dict == "dOut":
            self.dOut[key].append(value)

    def update_edge(self, key, value):
        self.edges[key] = value

    def remove_value(self, dict, key, value):
        if dict == "dIn":
            self.dIn[key].pop(self.dIn[key].index(value))
        elif dict == "dOut":
            self.dOut[key].pop(self.dOut[key].index(value))
