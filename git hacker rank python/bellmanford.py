class Vertex:
    def __init__(self,value):
        self.adj_list = []
        self.value = value
        self.parent = -1
        self.distance = 9999

class Graph:
    def __init__(self, size):
        self.size = size
        self.V = [Vertex(i+1) for i in range(size)]

    def relax(self, u, v, w):
        if self.V[v].distance > self.V[u].distance + w[u][v]:
            self.V[v].distance = self.V[u].distance + w[u][v]
            self.V[v].parent = self.V[u].value

    def add_edge(self, from_vertex, to_vertex):
        self.V[from_vertex].adj_list.append(to_vertex)

    def bellman_ford(self, w, s):
        self.V[s].distance = 0

        for _ in range(self.size - 1):
            for u in range(self.size):
                for v in self.V[u].adj_list:
                    if w[u][v] != 0:
                        self.relax(u, v, w)

        for u in range(self.size):
            for v in self.V[u].adj_list:
                if self.V[v].distance > self.V[u].distance + w[u][v]:
                    return False

        return True

    def show_graph(self):
        print("\nVertex | Parent | Distance |")
        print("********************************")

        for i in range(self.size):
            if self.V[i].parent == -1:
                print(f"{self.V[i].value:6} | Source  | {self.V[i].distance:8} |")
            else:
                print(f"{self.V[i].value:6} | {self.V[i].parent:6} | {self.V[i].distance:8} |")

        print("********************************")

if __name__ == "__main__":
    MAX = 20
    # n = int(input("eneter the total node"))
    # b = [[0]*(n) for _ in range(n)]
    # for i in range(n):
    #     for j in range(n):
    #         b[i][j] = int(input("enter the distance if no connection then it is 0:"))
    n = 5
    b = [
        [0, 6, 0, 0, 7],
        [0, 0, 5, -4, 8],
        [0, -2, 0, 0, 0],
        [2, 0, 7, 0, 0],
        [0, 0, -3, 9, 0]
    ]

    g = Graph(n)

    for i in range(n):
        for j in range(n):
            if b[i][j] != 0:
                g.add_edge(i, j)

    s = 0
    res = g.bellman_ford(b, s)

    if res:
        print("\n\nSingle Source Shortest Path (Bellman-Ford Algorithm) Result:")
        g.show_graph()
    else:
        print("\nNegative Weight Cycle is Present. \nSo, Could Not find Shortest Path....")

#summa test
