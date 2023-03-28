class Solution:
    shop=Shop()
    def __init__(self,shop):
        self.shop=shop
    
    def find(self,n,k):
        def search(maxi, coins):
            lo, hi = 0, maxi
            while lo < hi:
                mi = lo+(hi-lo)//2
                if self.shop.get(mi) > coins:
                    hi = mi
                else:
                    lo = mi+1
            return lo-1
            
        ans = 0
        while True:
            n = search(n, k)
            if n == -1:
                return ans
            maxv = self.shop.get(n)
            ans += k//maxv
            k %= maxv
        return ans
      
"""This code implements a function find() that takes two arguments n and k. It uses a binary search algorithm to find the maximum value less than or equal to n for which the shop's price is less than or equal to k. It repeats this process until n is less than 0 or there are no more items that can be bought with the remaining k.

Specifically, search(maxi, coins) is a helper function that takes in maxi and coins as parameters. It performs a binary search on the shop's inventory up to index maxi to find the highest item that can be purchased with coins amount of money. It returns the index of the item found.

In the find(n, k) function, a variable ans is initialized to 0. Then, the loop keeps searching for the highest-priced item that can be bought with the remaining money in k. For each item found, the code computes how many items of that type can be bought with k and subtracts the price of these items from k. The count of items is added to ans. The loop stops when n is less than 0 or there are no more items that can be bought with the remaining k.

Finally, the function returns ans, which represents the total number of items that can be bought.
"""
