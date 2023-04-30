        l=[]
        for n1,n2 in intervals:
            l.append((n1,-1))
            l.append((n2,1))
        l.sort()
        
        n=0
        ans=-1
        for n1,n2 in l:
            if n2==-1:
                n+=1
            else:
                if n>=k:
                    ans=max(ans,n1)
                n-=1
        return ans
      
"""This code is finding the largest endpoint among all the intervals such that there are at least k intervals that contain that endpoint.

The input intervals is a list of tuples, each representing an interval with two numbers, the start and end points.

First, the code creates a list l which contains pairs (n1, -1) and (n2, 1) for each interval (n1, n2) in intervals. The -1 is used to indicate the start of an interval and 1 to indicate the end of an interval. The list is then sorted by the first element of each pair.

Next, the code loops through the sorted list l. For each pair, it checks if the second element is -1. If so, it increments a counter n. If the second element is 1, it decrements n. If n is greater than or equal to k after decrementing, the code updates ans to be the maximum of ans and the first element of the current pair n1.

Finally, the code returns ans, which is the largest endpoint that satisfies the condition of having at least k intervals containing that endpoint."""
