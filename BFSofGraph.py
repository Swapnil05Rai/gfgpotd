class Solution:
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        ans=[]
        seen=set()
        q=[0]
        seen.add(0)
        while q:
            nq=[]
            for i in q:
                ans.append(i)
                for j in adj[i]:
                    if j not in seen:
                        nq.append(j)
                        seen.add(j)
            q=nq
        return ans
