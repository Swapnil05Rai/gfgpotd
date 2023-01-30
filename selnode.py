class Solution:
    def dfs(self, graph, u, p):
        exc, inc = 0, 1    
        for v in graph[u]:
            if v != p:
                cexc, cinc = self.dfs(graph, v, u)
                exc += cinc
                inc += min(cinc, cexc)
        return exc, inc
                
                
    def countVertex(self, N, edges):
        graph = [[] for _ in range(N)]
        for u,v in edges:
            graph[u-1].append(v-1)
            graph[v-1].append(u-1)
            
        return min(self.dfs(graph, 0, -1))
 


"""The countVertex() method takes in two arguments:

N: The number of nodes in the graph.
edges: A list of lists representing the edges in the graph. Each sublist contains the indices (1-based) of the two nodes that are connected by an edge.
The method first converts the edges from 1-based indices to 0-based indices. It does this by subtracting 1 from the indices in the edges.

Then it creates a graph represented by an adjacency list,
where each element of the list represents a node and its value is a list of the nodes that are directly connected to it.

Then it call the dfs method which takes three arguments:

graph: the graph represented by the adjacency list.
u: the current node being visited.
p: the parent node of the current node.
The dfs method is used to traverse the graph recursively starting from node 0, and keeping track of two values for each node:

exc: the minimum number of nodes that need to be removed to make the subtree rooted at that node not contain the root.
inc: the minimum number of nodes that need to be removed to make the subtree rooted at that node contain the root.
The dfs method starts by initializing exc and inc to 0 and 1, respectively. Then it loops through the children of the current node, and for each child v, 
it calls dfs recursively and updates exc and inc accordingly.

Finally, the countVertex() method returns the minimum of the two values returned by the dfs method,
which represents the minimum number of nodes that need to be removed to make the graph not contain the root."""
