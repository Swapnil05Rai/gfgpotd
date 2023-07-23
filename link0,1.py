def segregate(self, head):
        counts, node = [0] * 3, head
        while node:
            counts[node.data] += 1
            node = node.next
        node, i = head, 0
        while node:
            while counts[i] == 0:
                i += 1
            node.data = i
            counts[i] -= 1
            node = node.next
        return head
