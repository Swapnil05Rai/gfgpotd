def LCA(root, n1, n2):
    a1 = []
    a2 = []
    def search(root, n, arr):
        if root is None:
            return
        if n == root.data:
            arr.append(root)
            return
        if n < root.data:
            arr.append(root)
            search(root.left, n, arr)
        if n > root.data:
            arr.append(root)
            search(root.right, n, arr)
    search(root, n1, a1)
    search(root, n2, a2)
    result = root
    for i in range(len(a1) - 1, -1, -1):
        if a1[i] in a2:
            result = a1[i]
            break
    return result
