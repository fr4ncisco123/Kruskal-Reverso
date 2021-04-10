
class Graph:
    def __init__(self, v):

        self.v = v
        self.adj = [0] * v
        self.edges = []
        for i in range(v):
            self.adj[i] = []

    def addEdge(self, u: int, v: int, w: int):
        self.adj[u].append(v) 
        self.adj[v].append(u) 
        self.edges.append((w, (u, v)))
  
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
  
        self.edges.sort(key = lambda a: a[0])
  
        mst_wt = 0 
  
        print("Edges in MST")
  
        for i in range(len(self.edges) - 1, -1, -1):
            u = self.edges[i][1][0]
            v = self.edges[i][1][1]
  
            self.adj[u].remove(v)
            self.adj[v].remove(u)
  
            if self.connected() == False:
                self.adj[u].append(v)
                self.adj[v].append(u)
  
                print("( %d, %d )" % (u, v))
                mst_wt += self.edges[i][0]
        print("Total weight of MST is", mst_wt)
  
if __name__ == "__main__":
  
    V = 9
    g = Graph(V)
  
    g.addEdge(0, 1, 4)
    g.addEdge(0, 7, 8)
    g.addEdge(1, 2, 8)
    g.addEdge(1, 7, 11)
    g.addEdge(2, 3, 7)
    g.addEdge(2, 8, 2)
    g.addEdge(2, 5, 4)
    g.addEdge(3, 4, 9)
    g.addEdge(3, 5, 14)
    g.addEdge(4, 5, 10)
    g.addEdge(5, 6, 2)
    g.addEdge(6, 7, 1)
    g.addEdge(6, 8, 6)
    g.addEdge(7, 8, 7)
  
    g.reverseDeleteMST()
