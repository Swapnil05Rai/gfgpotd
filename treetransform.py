from typing import List


class Solution:

    def solve(self, N : int, p : List[int]) -> int:

        # code here

        cnt=0

        dict={}

        for i in p:

            if i== (-1) or i ==0:

                continue

            else:

                if i not in dict:

                    dict[i]=1

                    cnt+=1

                dict[i]+=1

        return cnt
