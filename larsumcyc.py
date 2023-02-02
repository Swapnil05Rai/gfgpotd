import sys
sys.setrecursionlimit(10**6)

class Solution():
    def dfs(self, graph, visited, u):
        if visited[u] == 2:
            return -1
        elif visited[u] == 1:
            res, cur = u, u
            while graph[cur] != u:
                cur = graph[cur]
                res += cur
            return res
        elif graph[u] != -1:
            visited[u] = 1
            res = self.dfs(graph, visited, graph[u])
            visited[u] = 2
            return res
        else:
            visited[u] = 2
            return -1
    
                
    def largestSumCycle(self, N, Edge):
        #your code goes here
        visited = [0]*N
        res = -1
        for u in range(N):
            res = max(res, self.dfs(Edge, visited, u))
        return res
      
      
"""The dfs method is a depth-first search that visits each node in the graph represented by the Edge array.
The visited array keeps track of whether a node has been visited, is currently being visited, or has already been visited. 
If a node has already been visited and is being visited again, it means a cycle has been formed, and the sum of the values of the nodes in the cycle is returned. 
If a node has not been visited and its next node (as defined by the Edge array) is -1, it means it's a dead-end and the value of -1 is returned.

The largestSumCycle method uses the dfs method to find the sum of the nodes in the largest cycle in the graph.
It does this by calling dfs for each node in the graph and keeping track of the maximum sum returned. The final result is returned by the method."""
