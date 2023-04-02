class Solution:
    def knightInGeekland(self, arr, start):

        m, n = len(arr), len(arr[0])
        q = [(start[0], start[1])]
        coins = []
        visited = {(start[0], start[1])}
        
        ds = [(r, c) for r in (-2, 2) for c in (-1, 1)] + [(r, c) for r in (-1, 1) for c in (-2, 2)]
        while q:
            s = 0
            nq = []
            for r0, c0 in q:
                s += arr[r0][c0]
                for dr, dc in ds:
                    r, c = r0+dr, c0+dc
                    if (r, c) not in visited and 0 <= r < m and 0 <= c < n:
                        nq.append((r, c))
                        visited.add((r, c))
            coins.append(s)
            q = nq
        
        cnt = 0
        ans = 0
        for i in range(len(coins)-1, -1, -1):
            if coins[i]+i < len(coins):
                coins[i] += coins[coins[i]+i]
            if coins[i] >= cnt:
                cnt = coins[i]
                ans = i
        return ans
    




"""This function solves the "Knight in Geekland" problem, which involves a knight on a chessboard moving in the L-shape pattern of a knight in chess. The chessboard has coins on some squares, and the knight collects all the coins it passes over. The function takes in the arr parameter, which is a two-dimensional list representing the chessboard, and start, which is a tuple (r, c) representing the row and column of the starting position of the knight.

The function first initializes some variables: m and n are the dimensions of the chessboard, q is a list containing the starting position of the knight, coins is a list that will contain the total coins collected by the knight at each step, and visited is a set containing the coordinates of all the squares that the knight has visited.

Next, the function uses ds to create a list of all possible moves for the knight, and it starts a while loop that will continue until the q list is empty.

Inside the while loop, the function initializes s to 0 and nq to an empty list. The loop then iterates over all the coordinates in the q list, collecting the coin on each square and updating the s variable. The loop then iterates over all possible moves for the knight and appends any new, unvisited coordinates to the nq list.

After each iteration of the while loop, the function appends the s variable to the coins list, and it sets q to the nq list.

Once the coins list has been populated, the function initializes cnt to 0 and ans to 0. The function then iterates over the coins list in reverse order, updating the value of each element by adding the value of the element at the index coins[i]+i (if it exists). The function then checks if the updated value of coins[i] is greater than or equal to cnt. If it is, the function updates cnt to coins[i] and ans to i.

Finally, the function returns ans, which is the index of the step where the knight collects the maximum number of coins."""
