from collections import deque

MAX = 20
INF = 99999


class Vertex:
    def __init__(self):
        self.adjlist = []
        self.value = 0
        self.color = "W"
        self.dist = INF
        self.parent = -1

def path_bfs(b, n, s, t, path):
    V = [Vertex() for _ in range(n)]
    
    for i in range(n):
        V[i].value = i
        V[i].color = "W"
        V[i].dist = INF
        V[i].parent = -1
    
    for i in range(n):
        for j in range(n):
            if b[i][j] != 0:
                V[i].adjlist.append(j)
    
    V[s].color = "G"
    V[s].dist = 0
    V[s].parent = -1

    Q = deque([s])

    while Q:
        c = Q.popleft()

        for u in V[c].adjlist:
            if V[u].color == "W":
                V[u].color = "G"
                V[u].dist = V[c].dist + 1
                V[u].parent = c
                Q.append(u)
        
        V[c].color = "B"

    cnt = 0
    path[cnt] = t
    cnt += 1

    while V[t].parent != -1:
        path[cnt] = V[t].parent
        cnt += 1
        t = V[t].parent
    
    path[:cnt] = reversed(path[:cnt])

    return cnt

def max_flow(b, n, s, t):
    path = [0] * MAX
    max_flow = 0

    while (cnt := path_bfs(b, n, s, t, path)) > 1:
        min_cap = INF

        for i in range(cnt - 1):
            u = path[i]
            v = path[i + 1]
            if b[u][v] < min_cap:
                min_cap = b[u][v]

        max_flow += min_cap

        for i in range(cnt - 1):
            u = path[i]
            v = path[i + 1]
            b[u][v] -= min_cap
            b[v][u] += min_cap

    return max_flow

if __name__ == "__main__":
    n = 10
    b = [
        [0, 12, 0, 0, 0, 20, 0, 3, 0, 0],
        [0, 0, 5, 0, 0, 0, 0, 0, 6, 0],
        [0, 0, 0, 13, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 12, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 10, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 3, 0, 0, 0, 0, 5],
        [0, 0, 0, 0, 0, 0, 4, 0, 4, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 0, 3],
        [0, 0, 0, 10, 0, 0, 0, 0, 0, 0]
    ]

    print(f"\n\n\tMaximum Flow From 0 to 3: {max_flow(b, n, 0, 3)}")
