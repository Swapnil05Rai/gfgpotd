class Solution:
    def finLength(self, n : int, color : List[int], radius : List[int]) -> int:
        stack = [[color[0],radius[0]]]
        i = 1
        while(i<n):
            if len(stack)!=0 and (stack[-1][0] == color[i] and stack[-1][1] == radius[i]):
                stack.pop()
            else:
                stack.append([color[i],radius[i]])
            i+=1
        return len(stack)
      
      
"""The solution uses a stack to keep track of the rods that can be used to make the longest possible rod. The algorithm starts by pushing the first rod (with color color[0] and radius radius[0]) to the stack.

Then, for each rod (starting from the second rod), the algorithm checks if the top rod in the stack has the same color and radius as the current rod. If it does, it means that we can remove the top rod from the stack, as it cannot be used to make the longest possible rod. Otherwise, we add the current rod to the stack.

Once we have processed all the rods, the length of the stack gives us the length of the longest possible rod that can be made using the given rods.

The time complexity of this algorithm is O(n), where n is the number of rods. This is because we process each rod exactly once."""
