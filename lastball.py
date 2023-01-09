
class Solution:
  def find_modified_bowl(self, bowls):
    # Start from the last bowl
    for i in range(len(bowls)-1, -1, -1):
      if bowls[i] < 9:
        # There is space in this bowl, so we add the marble
        bowls[i] += 1
        return i + 1 # Return one-based index
      else:
        # No space in this bowl, so we set it to zero and move on to the next bowl
        bowls[i] = 0
    return -1 # All bowls are full

  def solve(self, N, A):
    return self.find_modified_bowl(A)


        
"""The solution uses a class called Solution that has a method called solve which takes two arguments: N and A. N is the number of bowls and A is a list of the number of marbles in each bowl.

The solve method first calls another method called find_modified_bowl, which takes a single argument: a list of the number of marbles in each bowl. This method loops through the bowls from the last bowl to the first bowl, and for each bowl it checks if there is space to add a marble. If there is space, it adds the marble and returns the index of that bowl. If there is no space, it sets the number of marbles in that bowl to zero and moves on to the next bowl. If all bowls are full, the method returns -1.

The solve method then returns the result of calling find_modified_bowl on the input list of marbles."""
