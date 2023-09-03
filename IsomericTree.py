import collections

class Solution:
    # Return True if the given trees are isomotphic. Else return False.
    def isIsomorphic(self, root1, root2): 
        #code here.
        if not root1 and not root2: return True
        que1,que2=deque(),deque()
        que1.append(root1)
        que2.append(root2)
        map1,map2=collections.defaultdict(list),collections.defaultdict(list)
        while que1:
            for _ in range(len(que1)):
                cur=que1.popleft()
                if cur.left:
                    que1.append(cur.left)
                    map1[cur.data].append(cur.left.data)
                if cur.right:
                    que1.append(cur.right)
                    map1[cur.data].append(cur.right.data)
        while que2:
            for _ in range(len(que2)):
                cur=que2.popleft()
                if cur.left:
                    que2.append(cur.left)
                    map2[cur.data].append(cur.left.data)
                if cur.right:
                    que2.append(cur.right)
                    map2[cur.data].append(cur.right.data)
        for i,j in map1.items():
            if i not in map2.keys():
                return False
            else:
                for v in j:
                    if v not in map2[i]:
                        return False
        return True

