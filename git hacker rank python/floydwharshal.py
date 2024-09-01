MAX = 20
INF = 99999
NIL = -1

def floyd_warshall(cost, n):
    dist = [[0] * (n+1) for _ in range(n+1)]
    parent = [[0] * (n+1) for _ in range(n+1)]

    # Initialize D and P matrices
    D = [[[0] * (n+1) for _ in range(n+1)] for _ in range(n+1)]
    P = [[[0] * (n+1) for _ in range(n+1)] for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, n+1):
            D[0][i][j] = cost[i][j]
            if D[0][i][j] == 0 or D[0][i][j] == INF:
                P[0][i][j] = NIL
            else:
                P[0][i][j] = i

    # Floyd-Warshall algorithm
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if D[k-1][i][k] + D[k-1][k][j] < D[k-1][i][j]:
                    D[k][i][j] = D[k-1][i][k] + D[k-1][k][j]
                    P[k][i][j] = P[k-1][k][j]
                else:
                    D[k][i][j] = D[k-1][i][j]
                    P[k][i][j] = P[k-1][i][j]

    # Final Dist and Parent matrices
    for i in range(1, n+1):
        for j in range(1, n+1):
            dist[i][j] = D[n][i][j]
            parent[i][j] = P[n][i][j]

    return dist, parent

def print_matrix(matrix, n, label):
    print(f"\n\n\t{label} Matrix:")
    for i in range(1, n+1):
        print("\t", end="")
        for j in range(1, n+1):
            if matrix[i][j] == INF:
                print("INF\t\t", end="")
            elif matrix[i][j] == NIL:
                print("NIL\t\t", end="")
            else:
                print(f"{matrix[i][j]}\t\t", end="")
        print()

def main():
    n = int(input("Enter the number of nodes: "))

    # Initialize the cost matrix
    cost = [[0] * (n+1) for _ in range(n+1)]

    print("Enter the cost matrix (use 99999 for INF):")

    for i in range(1, n+1):
        for j in range(1, n+1):
            if i != j:
                a = input(f"Cost from node {i} to node {j}: ")
                if a == "INF" :
                    cost[i][j] = 99999
                else:
                    cost[i][j] = int(a)
            else:
                cost[i][j] = 0
            
             
    dist, parent = floyd_warshall(cost, n)

    print_matrix(dist, n, "Distance")
    print_matrix(parent, n, "Parent")

if __name__ == "__main__":
    main()
