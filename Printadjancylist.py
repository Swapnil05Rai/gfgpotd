def printGraph(self, V : int, edges : List[List[int]]) -> List[List[int]]:
    adj=[[] for _ in range(V)]
    for u,v in edges:
        adj[u].append(v)
        adj[v].append(u)
    return adj
