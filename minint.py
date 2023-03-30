class Solution:
    def minimumInteger(self, N : int, A : List[int]) -> int:
        # code here
        S=0
        y=0
        pr=1
        sum=0
        ans=0
        for x in A:
            if(ans<x):
                ans=x
            
            sum=sum+x
            
        
        for y in A:
            pr=y*N
            if(pr==sum):
                return y
            if(pr>=sum):
                if(ans>y):
                    ans=y
                
        return ans
      
"""This is a solution to the problem of finding the minimum integer y such that the sum of all multiples of y in the list A is equal to N times y.

The algorithm iterates over the elements in A and keeps track of the maximum element ans and the sum of all elements sum. Then, it iterates over the elements in A again and calculates the product pr of y and N. If pr is equal to sum, it means that y is the solution and the algorithm returns y. Otherwise, if pr is greater than sum, it means that y is too large, so the algorithm checks if ans is smaller than y. If ans is smaller, it means that ans is a better solution, so the algorithm updates ans with y. Finally, the algorithm returns ans.

In summary, the algorithm first checks the trivial case where the sum of all elements is equal to N times the maximum element, and if it is not the case, it tries to find the minimum integer that satisfies the condition by checking all the possible integers starting from the maximum element."""
