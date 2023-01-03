from bisect import bisect_left
class Solution:
    def removeStudents(self, H, N):
        # code here
        ans = []
        for st in H:
            pi = bisect_left(ans, st)
            if pi >= len(ans):
                ans.append(st)
            else:
                ans[pi] = st
        return N-len(ans)
      
  """The solution uses the Longest Increasing Subsequence (LIS) algorithm to find the minimum number of students to be removed such that the maximum possible number of students can see the assembly.

The LIS algorithm works by maintaining a sorted list of the elements seen so far. For each element in the array H, it finds the position at which the element should be inserted into the list in order to keep the list sorted. If the element is the largest seen so far, it is appended to the list. Otherwise, the element at the insertion position is replaced with the new element.

At the end, the length of the list is the size of the longest increasing subsequence in H. The minimum number of students to be removed is then calculated by subtracting the length of the list from the total number of students N."""
