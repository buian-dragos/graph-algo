class Ui:
    def __init__(self, service):
        self.serv = service

    def print_menu(self):                                                                                         # NOQA
        print()
        print("1. Read file")
        print("2. Write to a file")
        print("3. Check if v is a vertex")
        print("4. Check if e is an edge")
        print("5. Vertex menu")
        print("6. Add edge")
        print("7. In degree of v")
        print("8. Out degree of v")
        print("9. Iterate outbound edges of a vertex")
        print("10.Iterate inbound edges of a vertex")
        print("11.Retrieve information of an edge")
        print("12.Modify information of an edge")
        print("13.Print dictionaries")
        print("14.Copy")
        print("15.Generate random graph")
        print("16.Print all edges")
        print("0. Exit")

    def run(self):
        while True:
            self.print_menu()
            choice = input("Choose an option: ")
            if choice == "1":
                file_name = input("File name: ")
                self.serv.read_file(file_name)
            elif choice == "2":
                file_name = input("File name: ")
                self.serv.write_file(file_name)
            elif choice == "3":
                v = input("v= ")
                if self.serv.is_vertex(v):
                    print(f"{v} is a vertex")
                    input()
                else:
                    print(f"{v} is not a vertex")
                    input()
            elif choice == "4":
                print("(edge format: \"v1,v2\")")
                edge = input("edge= ")
                if self.serv.is_edge(edge):
                    print(f"{edge} is an edge")
                    input()
                else:
                    print(f"{edge} is not an edge")
                    input()
            elif choice == "5":
                while True:
                    print("1. Add vertex")
                    print("2. Number of vertices")
                    print("3. Iterate vertices")
                    print("4. Remove vertex")
                    print("0. Return to menu")
                    v_comm = input("Choose an option: ")
                    if v_comm == "1":
                        v = input("v= ")
                        self.serv.add_vertex(v)
                    elif v_comm == "2":
                        print(f"There are {self.serv.number_of_vertices()} vertices")
                        input()
                    elif v_comm == "3":
                        self.serv.iterate_vertices()
                    elif v_comm == "4":
                        v = input("Vertex: ")
                        self.serv.remove_vertex(v)
                    elif v_comm == "0":
                        break
                    else:
                        print("Invalid command")
            elif choice == "6":
                print("(edge format: \"v1,v2\")")
                edge = input("edge= ")
                value = input("value= ")
                self.serv.add_edge(edge, value)
            elif choice == "7":
                v = input("v= ")
                print(f"The in degree of vertex {v} is {self.serv.in_degree(v)}")
                input()
            elif choice == "8":
                v = input("v= ")
                print(f"The out degree of vertex {v} is {self.serv.out_degree(v)}")
                input()
            elif choice == "9":
                v = input("v= ")
                self.serv.iterate_outbound(v)
            elif choice == "10":
                v = input("v= ")
                self.serv.iterate_inbound(v)
            elif choice == "11":
                print("(edge format: \"v1,v2\")")
                edge = input("edge= ")
                print(self.serv.get_value_of_edge(edge))
                input()
            elif choice == "12":
                print("(edge format: \"v1,v2\")")
                edge = input("edge= ")
                new_value = input("new_value= ")
                self.serv.modify_value_of_edge(edge, new_value)
            elif choice == "13":
                print(self.serv.print_dictionaries())
                input()
            elif choice == "14":
                print("Not implemented")
                input()
            elif choice == "15":
                no_vert = int(input("number_of_vertices= "))
                no_edges = int(input("number_of_edges= "))
                self.serv.generate_random(no_vert, no_edges)
            elif choice == "16":
                print(self.serv.print_edges())
                input()
            elif choice == "0":
                exit()
            else:
                print("Invalid input")
