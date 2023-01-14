from itertools import accumulate
class Solution:
    def maximumToys(self,N,A,Q,Queries):
        def _count_consecutive():
            Con = [1]*N
            c = 1
            for i in range(1, N):
                if S[i] != S[i-1]: c=1; continue
                c+=1
                Con[i] = c
            return Con
        
        def _calc_cost(m):
            sum_cost = Acc[m]
            Concnt = Con[m]
            mv = S[m]
            skip_cnt = same_val_cnt = 0
            for skip in skips:
                if skip < mv:
                    sum_cost -= skip
                    skip_cnt += 1
                elif skip == mv and same_val_cnt < Concnt:
                    sum_cost -= skip
                    skip_cnt += 1
                    same_val_cnt += 1
                else:
                    break
            return sum_cost, skip_cnt
            
        S = sorted(A)
        Con = _count_consecutive()
        Acc = list(accumulate(S))
        ans = []
        for q in Queries:
            C, skips = q[0], sorted([ A[i-1] for i in q[2:] ])
            L, R, skip_cnt = 0, N-1, 0
            while L<=R:
                m = (L+R)//2
                v, skip_cnt = _calc_cost(m)
                if v <= C: L = m+1
                elif v > C: R = m-1
            ans.append(R+1-skip_cnt)
        return ans
      
      
"""This is a binary search algorithm that finds the maximum number of toys that can be purchased within a given budget.
   The algorithm first sorts the toys by price, then uses a binary search to find the largest number of toys that can be purchased within the budget. 
   The "skips" variable keeps track of the toys that have been removed from the original list of toys, 
   and the "_calc_cost" function calculates the total cost of the toys and the number of skips. 
   The final result is the maximum number of toys that can be purchased within the budget, minus the number of skips.
"""
