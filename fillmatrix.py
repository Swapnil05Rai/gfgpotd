def minIteration(N, M, x, y):
    x -= 1
    y -= 1
    left_top = x + y
    left_bottom = (N - 1 - x) + y
    right_top = x + (M - 1 - y)
    right_bottom = (N - 1 - x) + (M - 1 - y)
    return max(left_top, left_bottom, right_top, right_bottom)

  
  
  """This code snippet is a C++ function that takes four integer parameters N, M, x, and y, and returns an integer.

The function first decrements the x and y values by 1, which adjusts the coordinates to be 0-indexed.

It then calculates the distances from the four corners of a rectangular grid to the point (x, y). Specifically, it calculates the distance to the top-left corner, the bottom-left corner, the top-right corner, and the bottom-right corner.

Finally, it returns the maximum of these four distances, which represents the number of iterations required to reach any of the four corners from the point (x, y).

The calculation of distances is based on the Manhattan distance, which is the sum of the horizontal and vertical distances between two points."""
