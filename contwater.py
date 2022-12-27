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
