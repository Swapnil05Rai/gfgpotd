def maxArea(A, le):
    max_area = 0
    left = 0
    right = le - 1
    while left < right:
        area = min(A[left], A[right]) * (right - left)
        max_area = max(max_area, area)
        if A[left] < A[right]:
            left += 1
        else:
            right -= 1
    return max_area

"""The function first initializes three variables:

max_area to store the maximum area found so far, initialized to 0
left to store the index of the current left line, initialized to the first element of the array
right to store the index of the current right line, initialized to the last element of the array
Then, it enters a while loop that continues as long as left is less than right. This is because the two pointers need to be distinct in order to form a valid container.

Inside the loop, the function first calculates the current area between the two lines using the formula min(A[left], A[right]) * (right - left). It then updates the max_area variable if the current area is larger than the maximum area found so far.

After that, the function compares the heights of the two lines and moves the pointer that points to the shorter line towards the other one. This is because the area of the container is determined by the shorter line, so we need to consider other pairs of lines that have a shorter line.

Finally, the function returns the maximum area found after the loop ends.

"""
