# Python3 program to find Minimum Spanning Tree
# of a graph using Reverse Delete Algorithm
  
# Graph class represents a directed graph
# using adjacency list representation
class Graph:
    def __init__(self, v):
  
        # No. of vertices
        self.v = v
        self.adj = [0] * v
        self.edges = []
        for i in range(v):
            self.adj[i] = []
  
    # function to add an edge to graph
    def addEdge(self, u: int, v: int, w: int):
        self.adj[u].append(v) # Add w to v�s list.
        self.adj[v].append(u) # Add w to v�s list.
        self.edges.append((w, (u, v)))
  
    def dfs(self, v: int, visited: list):
  
        # Mark the current node as visited and print it
        visited[v] = True
  
        # Recur for all the vertices adjacent to
        # this vertex
        for i in self.adj[v]:
            if not visited[i]:
                self.dfs(i, visited)
  
    # Returns true if graph is connected
    # Returns true if given graph is connected, else false
    def connected(self):
        visited = [False] * self.v
  
        # Find all reachable vertices from first vertex
        self.dfs(0, visited)
  
        # If set of reachable vertices includes all,
        # return true.
        for i in range(1, self.v):
            if not visited[i]:
                return False
  
        return True
  
    # This function assumes that edge (u, v)
    # exists in graph or not,
    def reverseDeleteMST(self):
  
        # Sort edges in increasing order on basis of cost
        self.edges.sort(key = lambda a: a[0])
  
        mst_wt = 0 # Initialize weight of MST
  
        print("Edges in MST")
  
        # Iterate through all sorted edges in
        # decreasing order of weights
        for i in range(len(self.edges) - 1, -1, -1):
            u = self.edges[i][1][0]
            v = self.edges[i][1][1]
  
            # Remove edge from undirected graph
            self.adj[u].remove(v)
            self.adj[v].remove(u)
  
            # Adding the edge back if removing it
            # causes disconnection. In this case this
            # edge becomes part of MST.
            if self.connected() == False:
                self.adj[u].append(v)
                self.adj[v].append(u)
  
                # This edge is part of MST
                print("( %d, %d )" % (u, v))
                mst_wt += self.edges[i][0]
        print("Total weight of MST is", mst_wt)
  
# Driver Code
if __name__ == "__main__":
  
    # create the graph given in above fugure
    V = 9
    g = Graph(V)
  
    # making above shown graph
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
  
# This code is contributed by
# sanjeev2552