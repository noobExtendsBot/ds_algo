class Vertex:
    def __init__(self, key):
        self.id = key
        # connected to dict will have verticies it is connected to
        # and weight of the edge
        self.connected_to = {}

    def add_neighbor(self, nbr, weight=0):
        self.connected_to[nbr] = weight

    def __str__(self):
        return f"{self.id} connected to {[x.id for x in self.connected_to]}"

    def get_connections(self):
        # for k, v in self.connected_to.items():
        #     print(k, v)
        # return self.connected_to.keys()
        # return [v for v in self.connected_to.values()]
        return [(k.get_id(), v) for k, v in self.connected_to.items()]

    def get_id(self):
        return self.id

    def get_weight(self, nbr):
        return self.connected_to[nbr]


class Graph:
    def __init__(self):
        self.vertex_list = {}
        self.num_of_vertices = 0

    def add_vertex(self, key):
        self.num_of_vertices += 1
        new_vertex = Vertex(key)
        self.vertex_list[key] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vertex_list:
            return self.vertex_list[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertex_list

    def add_edge(self, f, t, weight=0):
        # here we'll use add_neighbor method
        # make sure nodes are in the master vertex list
        if f not in self.vertex_list:
            new_vertex = self.add_vertex(f)
        if t not in self.vertex_list:
            new_vertex = self.add_vertex(t)
        self.vertex_list[f].add_neighbor(self.vertex_list[t], weight)

    def get_vertices(self):
        return self.vertex_list.keys()

    def __iter__(self):
        # iterate over all the vertex objects in the graph
        return iter(self.vertex_list.values())


if __name__ == "__main__":
    g = Graph()
    for i in range(6):
        g.add_vertex(i)
    print(g.get_vertices())
    g.add_edge(0, 1, 5)
    g.add_edge(0, 5, 2)
    g.add_edge(1, 2, 4)
    g.add_edge(2, 3, 9)
    g.add_edge(3, 4, 7)
    g.add_edge(3, 5, 3)
    g.add_edge(4, 0, 1)
    g.add_edge(5, 2, 1)
    g.add_edge(5, 4, 8)
    for obj in g:
        print(obj.get_id(), obj.get_connections())
    #     for w in v.get_connections():

    #         # print(v.get_id(), nbr, w.get_weight(nbr))
