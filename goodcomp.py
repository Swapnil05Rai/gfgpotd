
import collections
from collections import deque
from collections import defaultdict
class Solution:
    def dfs(self, graph, visited, u):
        res = [u]
        visited[u] = True
        for v in graph[u]:
            if not visited[v]:
                res.extend(self.dfs(graph, visited, v))
        return res
                
    def findNumberOfGoodComponent(self, V, adj):
        visited = [False]*(V+1)
        res = 0
        for u in range(1, V+1):
            if not visited[u]:
                nodes = self.dfs(adj, visited, u)
                if all(len(adj[node]) == len(nodes)-1 for node in nodes):
                    res += 1
        return res
      
      
      
"""This is a Python implementation of a solution to find the number of "good components" in a given graph. A "good component" is defined as a connected component of the graph in which all nodes except the central one have the same degree.

The solution makes use of a depth-first search (DFS) algorithm to traverse the graph and identify the connected components. The DFS function takes in the graph, the visited array, and the starting node u as input parameters. It returns the list of nodes in the connected component containing u.

The main function, findNumberOfGoodComponent, initializes the visited array and loops through all nodes in the graph. For each unvisited node, it performs a DFS and checks whether the nodes in the resulting connected component form a good component. If so, it increments the count of good components. The check is performed by verifying that all nodes in the connected component have the same degree, except for the central node which has one less degree.

Finally, the function returns the count of good components found in the graph."""
