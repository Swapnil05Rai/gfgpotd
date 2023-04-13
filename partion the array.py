def minDifference(self, N, A): 

    # Initialize an array 'sums' with N+1 elements
    sums = [0]*(N+1)
    
    # Iterate over the input list A and compute the running sum for each element
    for i, e in enumerate(A):
        sums[i+1] = sums[i]+e
    
    # Define a helper function 'search' that takes two arguments, l and r (which are indices in 'sums' list)
    def search(l, r):
        # Initialize two pointers 'lo' and 'hi' with the given left and right indices
        lo, hi = l, r
        
        # Perform a binary search on the 'sums' list between indices 'l' and 'r'
        while lo < hi:
            # Compute the midpoint 'm' between 'lo' and 'hi'
            m = lo+(hi-lo)//2
            
            # Compute the sum of elements in the left partition between 'l' and 'm'
            lp = sums[m+1]-sums[l]
            
            # Compute the sum of elements in the right partition between 'm+1' and 'r'
            rp = sums[r+1]-sums[m]
            
            # Check if the left partition is greater than or equal to the right partition
            if lp >= rp:
                # If yes, then move 'hi' to 'm'
                hi = m
            else:
                # If no, then move 'lo' to 'm+1'
                lo = m+1
        
        # Compute the sums of the left and right partitions that correspond to the minimum and maximum values
        v1, v2 = sums[lo+1]-sums[l], sums[r+1]-sums[lo+1]
        
        # If the left partition has more than one element, then check for the next position where left-part <= right-part
        if lo > l:
            v3, v4 = sums[lo] - sums[l], sums[r+1] - sums[lo]
            if abs(v2-v1) > abs(v4-v3): 
                return min(v3, v4), max(v3, v4)
        
        # Return the minimum and maximum values of the two partitions
        return min(v1, v2), max(v1, v2)
        
    # Initialize the answer variable with infinity
    ans = float('inf')
    
    # Iterate over the indices from 1 to N-2 (both inclusive)
    for i in range(1, N-2):
        # Call the 'search' function with two indices as arguments: 0 and i for the left partition, and i+1 and N-1 for the right partition
        minv1, maxv1 = search(0, i)
        minv2, maxv2 = search(i+1, N-1)
        
        # Compute the minimum difference between the maximum and minimum values of the two partitions and update the answer variable
        ans = min(ans, max(maxv1, maxv2)-min(minv1, minv2))
    
    # Return the final answer
    return ans
