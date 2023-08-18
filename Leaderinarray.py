def leaders(self, A, N):
        leaders_list = []
        max_right = A[N - 1]  # The rightmost element is always a leader
        leaders_list.append(max_right)
        
        # Iterate through the array from right to left
        for i in range(N - 2, -1, -1):
            if A[i] >= max_right:
                max_right = A[i]
                leaders_list.append(max_right)
                
        # Reverse the list to maintain the order of appearance
        leaders_list.reverse()
        return leaders_list
