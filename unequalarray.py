from typing import List
class Solution:
    def solve(self, N : int, A : List[int], B : List[int]) -> int:
        # code here
        if sum(A)!=sum(B):
            return -1
        oa=[];ea=[]
        ob=[];eb=[]
        for i in A:
            if i%2:
                oa.append(i)
            else:
                ea.append(i)
        for i in B:
            if i%2:
                ob.append(i)
            else:
                eb.append(i)
        if len(oa)!=len(ob) or len(ea)!=len(eb):
            return -1
        oa.sort()
        ea.sort()
        ob.sort()
        eb.sort()
        ans=0
        for i in range(len(oa)):
            x=abs(oa[i]-ob[i])
            ans+=(x//2)
        for i in range(len(eb)):
            x=abs(eb[i]-ea[i])
            ans+=(x//2)
        
        return ans//2
      
"""This is a solution to a problem where we need to determine if two lists of integers can be transformed into each other by performing swaps between even numbers and swaps between odd numbers.

The function solve takes three arguments, N, A, and B. N represents the length of the lists, A and B are the lists of integers that need to be transformed.

The first condition checked is whether the sum of elements in A is equal to the sum of elements in B. If this condition fails, the function returns -1, indicating that no transformation is possible.

Then, the lists oa and ea are created to store the odd and even integers in A, respectively. Similarly, the lists ob and eb are created to store the odd and even integers in B. The lengths of oa, ob, ea, and eb must be equal for a transformation to be possible.

The lists oa, ea, ob, and eb are sorted in non-decreasing order. Then, a loop iterates over the length of oa. For each i in this loop, the difference between oa[i] and ob[i] is computed and added to a running total. This difference is then divided by 2 and added to the ans variable, which is the total number of swaps needed.

A similar loop is run over the length of eb. The difference between eb[i] and ea[i] is computed and added to the running total, and then the difference is divided by 2 and added to ans.

Finally, the function returns ans divided by 2. This is because each swap requires two steps, and we have counted each step separately in the loops."""
