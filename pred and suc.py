class Solution:
    def findPreSuc(self, root, pre, suc, key):
        node = root
        while node:
            if key < node.key:
                suc = node
                node = node.left
            elif key > node.key:
                pre = node
                node = node.right
            else:
                break
        if node:
            if node.left:
                pre = node.left
                while pre.right:
                    pre = pre.right
            if node.right:
                suc = node.right
                while suc.left:
                    suc = suc.left
        return pre, suc
