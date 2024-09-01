from collections import deque

MAX = 20
INF = 99999


class Vertex:
    def __init__(self):
        self.adjlist = []
        self.value = 0
        self.color = "W" 
        self.dist =99999
        self.parent = -1

def pathbfs(b,n,s,t,p):
    V = [Vertex() for _ in range(n)]
    
    for i in range(n):
        V[i].value = i
        V[i].color = "W"
    
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
    
    cnt =0
    p[cnt] = t
    cnt += 1

    while V[t].parent != -1:
        p[cnt] = V[t].parent
        cnt += 1
        t = V[t].parent

    p[:cnt] = reversed(p[:cnt])

    return cnt

def Maf(b, n,s,t):
    maxFlow =0
    p = [0]*MAX

    while (cnt := pathbfs(b,n,s,t,p)) > 1:
        minCap = INF

        for i in range(cnt-1):
            u = p[i]
            v = p[i+1]
            if b[u][v] < minCap:
                minCap = b[u][v]

        maxFlow  += minCap

        for i in range(cnt-1):
            u = p[i]
            v = p[i+1] 
            b[u][v] -= minCap     
            b[v][u] += minCap

    return maxFlow  

if __name__ == "__main__":
    r = 10
    c = [
        [0,12,0,0,0,20,0,3,0,0],
         [0,0,5,0,0,0,0,0,6,0],
         [0,0,0,13,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,12,0,0,0,0,0,0],
         [0,0,0,0,10,0,5,0,0,0],
         [0,0,0,0,3,0,0,0,0,5],
         [0,0,0,0,0,0,4,0,4,0],
         [0,0,3,0,0,0,0,0,0,3],
         [0,0,0,10,0,0,0,0,0,0]
         ]
    res = Maf(c,r,0,3)
    print(f"MAX Flow from 0 to 3: {res}")





