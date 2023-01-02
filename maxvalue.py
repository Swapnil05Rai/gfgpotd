class Solution:
    def maximumValue(self, root: Node) -> List[int]:
        v = []
        def tra(node: Node, level: int):
            if node is None:
                return
            if len(v) == level:
                v.append([node.data])
            else:
                v[level].append(node.data)
            tra(node.left, level+1)
            tra(node.right, level+1)

        v.clear()
        ans = []
        tra(root, 0)
        for i in v:
            ans.append(max(i))
        return ans

     
 
