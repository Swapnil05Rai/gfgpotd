def nearestSmallestTower(self, A):
        def _pre(r, out):
            stk = [(A[r.start], r.start)]
            for i in r[1:]:
                v = A[i]
                while stk and stk[-1][0] >= v: stk.pop()
                out[i] = INV if not stk else stk[-1][1]
                stk.append((v,i))
        
        N, INV = len(A), 10**9
        LL, LR = [INV]*N, [INV]*N
        ans = [-1] * N
        _pre(range(N), LL)
        _pre(range(N-1, -1, -1), LR)
        for i in range(N):
            if LL[i] == LR[i] == INV: continue
            Ldif, Rdif = abs(i-LL[i]), abs(LR[i]-i)
            if Ldif < Rdif: ans[i] = LL[i]
            elif Ldif > Rdif: ans[i] = LR[i]
            elif A[LL[i]] <= A[LR[i]]: ans[i] = LL[i]
            else: ans[i] = LR[i]
        return ans
      
"""This function takes in a list A of integers and returns a list ans of integers of the same length, where ans[i] is the index of the nearest element to the left of A[i] that is smaller than A[i]. If there is no such element, ans[i] will be -1.

The function starts by defining a helper function _pre that takes in a range of indices r and a list out. The purpose of this function is to precompute the nearest smaller element to the left of each element in the range r and store it in the corresponding position in out. To do this, it uses a stack stk to keep track of elements in A that are smaller than the current element being processed. Starting from the first element in r, it pushes this element onto the stack along with its index. For each subsequent element, it pops elements from the stack until it finds an element that is smaller than the current element. The index of this smaller element is then stored in out at the corresponding position. If the stack is empty, this means there is no smaller element to the left, so the value INV (which is a large number) is stored instead. The function then appends the current element and its index to the stack, and moves on to the next element in r. The function then does the same thing again, but with r in reverse order, to compute the nearest smaller element to the right of each element in A.

Next, the function initializes the lists LL, LR, and ans to be lists of length N (where N is the length of A) filled with the value INV and -1, respectively. It then calls _pre on the range range(N) with LL as the output list, and on the range range(N-1, -1, -1) with LR as the output list. This precomputes the nearest smaller element to the left and right of each element in A.

Finally, the function loops through each element in A and checks whether the nearest smaller element to the left and right of that element is valid (i.e. not equal to INV). If only one of these elements is valid, the index of that element is stored in ans at the corresponding position. If both elements are valid, the function computes the difference between the current index and each of these elements, and chooses the one that is closer. If both elements are equidistant, it chooses the smaller one (i.e. the one with the smaller value in A). The index of the chosen element is then stored in ans at the corresponding position. If neither element is valid, ans[i] is left as -1. Once all elements have been processed, ans is returned."""
