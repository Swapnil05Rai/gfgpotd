def fourSum(self, arr, k):
        from collections import defaultdict
        
        n = len(arr)
        d = defaultdict(list)
        for i in range(n - 1):
            for j in range(i + 1, n):
                d[arr[i] + arr[j]].append((i, j))
        output = set()
        visited = set()
        for s, ijs in d.items():
            if s in visited:
                continue
            r = k - s
            if r not in d:
                continue
            visited.add(r)
            for i, j in ijs:
                for kl in d[r]:
                    if i not in kl and j not in kl:
                        output.add(tuple(sorted(
                            (arr[i], arr[j], arr[kl[0]], arr[kl[1]])
                        )))
        return sorted(output)
