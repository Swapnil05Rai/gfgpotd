class Solution:
    def avoidExlosion(self, mix, n, danger, m):
        
        arr = [i for i in range(n+1)]
        def union(i, j):
            r1, r2 = find(i), find(j)
            if r1 != r2:
                arr[r1] = r2
            return r2
        def find(i):
            while i != arr[i]:
                i = arr[i]
            return i
            

        ans = []
        for x, y in mix:
            rx, ry = find(x), find(y)
            for p, q in danger:
                rp, rq = find(p), find(q)
                if (rx, ry) == (rp, rq) or (rx, ry) == (rq, rp):
                    ans.append("No")
                    break
            else:
                union(rx, ry)
                ans.append("Yes")
        return ans
      
      
      
"""The avoidExlosion function takes two lists mix and danger, where mix represents pairs of chemicals that can be mixed, and danger represents pairs of chemicals that cannot be mixed. The function returns a list of strings, where each string is either "Yes" or "No", indicating whether it is safe to mix the corresponding pair of chemicals in mix.

The function first initializes an array arr that represents a disjoint set data structure. The union function merges two sets by assigning the root of one set to the root of the other set. The find function finds the root of a set by following the parent pointers until it reaches the root.

For each pair of chemicals in mix, the function checks whether they are in the same set by finding their roots using the find function. If the chemicals are in different sets, the function merges the sets using the union function and appends "Yes" to the output list. If the chemicals are in the same set, the function appends "No" to the output list.

Finally, the function returns the output list containing the "Yes" and "No" strings indicating whether it is safe to mix each pair of chemicals in mix."""
