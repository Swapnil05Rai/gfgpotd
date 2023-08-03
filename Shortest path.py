from typing import List

from collections import defaultdict

import heapq

class Solution:

    def shortestPath(self, n : int, m : int, edges : List[List[int]]) -> List[int]:

        adj = defaultdict(list)

        for i,j,k in edges:

            adj[i].append([j,k])

        vis = [float('inf')]*(n)

        vis[0] = 0

        heap = [0]

        while(heap):

            node = heapq.heappop(heap)

            for it in adj[node]:

                adjNode = it[0]

                wt = it[1]

                if vis[adjNode]>wt+vis[node]:

                    vis[adjNode] = wt+vis[node]

                    heapq.heappush(heap,adjNode)

        for i in range(len(vis)):

            if vis[i]==float('inf'):

                vis[i]=-1

        return vis
