from typing import List
from collections import Counter
class Fenwick:
    def __init__(self, n):
        self.T = [[0]*26 for _ in range(n)]
        self.n = n
        self.F = lambda x: x&(x+1)
        self.H = lambda x: x|(x+1)

    def update(self, ind, c, delta):
        c = ord(c) - ord('a')
        while ind < self.n:
            self.T[ind][c] += delta
            ind = self.H(ind)

    def query(self, ind):
        result = [0]*26
        while ind >= 0:
            for c in range(26):
                result[c] += self.T[ind][c]
            ind = self.F(ind) - 1
        return result

    def range_query(self, left, right):
        return [r- l for r, l in zip(self.query(right), self.query(left-1))]

class Solution:
    def easyTask(self,n,s,q,queries) -> List[int]:
        tree = Fenwick(n)
        s = list(s)
        for ind, c in enumerate(s):
            tree.update(ind, c, 1)

        res = []
        for query in queries:
            if query[0] == '1':
                ind, char = int(query[1]), query[2]
                tree.update(ind, s[ind], -1)
                s[ind] = char
                tree.update(ind, s[ind], 1)
            else:
                left, right, k = int(query[1]), int(query[2]), int(query[3])
                counter = tree.range_query(left, right)

                for c in range(25, -1, -1):
                    if k > counter[c]:
                        k -= counter[c]
                    else:
                        res.append(chr(c + ord('a')))
                        break
        return res

"""This code defines a Fenwick class that implements a Fenwick tree for range updates and range queries of an array of 26 characters. The easyTask function then uses this class to perform updates and queries on a given string s and a list of queries queries.
The Fenwick class constructor initializes the tree with a 2D list of zeros with size n by 26, where n is the length of the array. The update method is used to add or subtract delta from the count of character c at position ind in the tree. The query method returns the cumulative count of each character up to position ind. The range_query method returns the count of each character within a given range.
In the easyTask function, the string s is converted to a list of characters, and each character is inserted into the Fenwick tree at its respective position. The function then loops through each query and either updates a character in the string or performs a range query on the Fenwick tree. For updates, the character at the given index is first removed from the tree, then replaced with the new character, and then re-added to the tree. For queries, the range_query method is used to count the frequency of each character within the given range. The code then loops through each character in descending order and subtracts its count from the k parameter until k becomes less than the count of a character. At that point, the character is added to the result list, and the loop is terminated. The result list is then returned."""
