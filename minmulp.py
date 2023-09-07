class Solution:
    
    def minimumMultiplications(self, arr : List[int], start : int, end : int) -> int:
        # code here
        dist=[float('inf')]*(100000+1)
        q=[[start,0]]
        mod=100000
        while(len(q)):
            ele,st=q.pop(0)
            if(ele==end):
                return st
            for j in arr:
                ele2=(j*ele)%mod
                if(dist[ele2]>st+1):
                    dist[ele2]=st+1
                    q.append([ele2,st+1])
        return -1
