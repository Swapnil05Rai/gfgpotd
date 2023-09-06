class Solution:
    
    def findMotherVertex(self, V, adj):
        visited = [False]* V
        last_visited = None
        
        for vertex in range(V):
            if not visited[vertex]:
                self.dfs(vertex, adj, visited)
                last_visited = vertex
                
        visited = [False]* V
        self.dfs(last_visited, adj, visited)
        
        for vertex in range(V):
            if not visited[vertex]:
                return -1
        return last_visited
        
    def dfs(self, s, adj, visited):
        visited[s] = True
        for neighbor in adj[s]:
            if not visited[neighbor]:
                self.dfs(neighbor, adj, visited)
