from typing import List


class Solution:
    def Rearrange(self, n : int, arr : List[int]) -> None:
        # code here
        pos=[]
        neg=[]
        for i in arr:
            if i<0:
                neg.append(i)
            else:
                pos.append(i)
        if len(neg)>0:
            for i in range(len(neg)):
                arr[i]=neg[i]
            for j in range(len(pos)):
                i+=1
                arr[i]=pos[j]
