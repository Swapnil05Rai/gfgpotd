 def makeChanges(self, N : int, K : int, target : int, coins : List[int]) -> bool:
        coins.sort()
        prev, cur = set(coins), set()
        for times in range(1, K):
            cur.clear()
            for v in prev:
                for c in coins:
                    if v + c > target: break
                    cur.add(v+c)
            prev, cur = cur, prev
        return target in prev
      
"""This code provides a solution to a problem where we need to determine whether it is possible to make a change of target amount with given denominations of coins coins using at most K coins.

The approach taken is a dynamic programming approach. We maintain two sets: prev and cur. Initially, we initialize prev with the given coins and cur as empty. Then, for each times from 1 to K-1, we iterate over each value in prev and each coin in coins, and calculate the sum of the current value and the current coin, and add it to cur if it is less than or equal to target. Finally, we swap the contents of prev and cur.

After the above loop, we check if target is in the final set prev. If it is, we return True, else we return False. This is because if target is reachable with at most K coins, it must be present in the final set prev.

Overall, this solution has a time complexity of O(N * K) where N is the number of given coins.

"""
