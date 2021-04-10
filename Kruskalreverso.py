
class Graph:
    def __init__(self, v):

        self.v = v
        self.adj = [0] * v
        self.Aresta = []
        for i in range(v):
            self.adj[i] = []

    def addAresta(self, u: int, v: int, w: int):
        self.adj[u].append(v) 
        self.adj[v].append(u) 
        self.Aresta.append((w, (u, v)))
  
    def dfs(self, v: int, visited: list):
        visited[v] = True
        for i in self.adj[v]:
            if not visited[i]:
                self.dfs(i, visited)

    def connected(self):
        visited = [False] * self.v 
        self.dfs(0, visited)
        for i in range(1, self.v):
            if not visited[i]:
                return False
  
        return True

    def reverseDeleteMST(self):  
        self.Aresta.sort(key = lambda a: a[0]) 
        mst_wt = 0  
        print("Arestas no MST")
        for i in range(len(self.Aresta) - 1, -1, -1):
            u = self.Aresta[i][1][0]
            v = self.Aresta[i][1][1]
            self.adj[u].remove(v)
            self.adj[v].remove(u)
            if self.connected() == False:
                self.adj[u].append(v)
                self.adj[v].append(u)
                print("( %d, %d )" % (u, v))
                mst_wt += self.Aresta[i][0]
        print("O peso total do MST e", mst_wt)
  
if __name__ == "__main__":
  
    V = 9
    g = Graph(V)
    g.addAresta(0, 1, 4)
    g.addAresta(0, 7, 8)
    g.addAresta(1, 2, 8)
    g.addAresta(1, 7, 11)
    g.addAresta(2, 3, 7)
    g.addAresta(2, 8, 2)
    g.addAresta(2, 5, 4)
    g.addAresta(3, 4, 9)
    g.addAresta(3, 5, 14)
    g.addAresta(4, 5, 10)
    g.addAresta(5, 6, 2)
    g.addAresta(6, 7, 1)
    g.addAresta(6, 8, 6)
    g.addAresta(7, 8, 7)
  
    g.reverseDeleteMST()
