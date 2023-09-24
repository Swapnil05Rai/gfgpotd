class Solution:
    def duplicates(self, arr, n): 
    ans = set()
    for i in range(n):
       arr[i] += 1
    for i in arr:
       if arr[abs(i)-1] < 0:
           ans.add(abs(i)-1)
       else:
           arr[abs(i)-1] *= -1
    return [-1] if len(ans) == 0 else sorted(ans)
