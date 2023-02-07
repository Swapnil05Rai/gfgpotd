def maxLength(arr, n):
    x = 0
    mx = 0
    z = 0
    par = 0
    ans = 0
    neg = -1
    last = -1
    for i in range(n): # loop through the elements of the array
        if arr[i] == 0: # if the current element is 0
            par = 0 # reset the parity
            neg = -1 # reset the index of the last negative number
            last = -1 # reset the index of the last non-zero element
        else: # if the current element is not 0
            if last == -1: # if the last non-zero element index has not been set
                last = i # set the last non-zero element index to i
            if neg == -1 and arr[i] < 0: # if the last negative element index has not been set and the current element is negative
                neg = i # set the last negative element index to i
            par = par ^ (1 if arr[i] < 0 else 0) # update the parity by XORing with 1 if the current element is negative and 0 otherwise
            if par == 0: # if the parity is 0
                ans = max(ans, i - last + 1) # update the answer to the max between the current answer and the length of the subarray from the last non-zero element to the current element
            else: # if the parity is not 0
                ans = max(ans, i - neg) # update the answer to the max between the current answer and the length of the subarray from the last negative element to the current element
    return ans # return the answer

  
"""It initializes the variables par and ans to 0, neg to -1 and last to -1.
These variables are used to keep track of the parity of the number of negative elements in the subarray,
the length of the longest subarray with a positive product,
the index of the last negative element in the subarray and the index of the last non-zero element in the subarray, respectively.

It then loops through the elements of the array and performs the following operations:
a. If the current element is 0, it resets par, neg, and last to 0, -1, and -1, respectively.
b. If the current element is non-zero:
i. If last is -1, it sets last to the current index.
ii. If neg is -1 and the current element is negative, it sets neg to the current index.
iii. It updates the parity by XORing par with 1 if the current element is negative and 0 otherwise.
iv. If the parity is 0, it updates ans to the maximum between ans and the length of the subarray from the last non-zero element to the current element.
v. If the parity is not 0, it updates ans to the maximum between ans and the length of the subarray from the last negative element to the current element.

It finally returns ans as the answer.
