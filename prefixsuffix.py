class Node:
    def __init__(self):
        self.nod=dict()
class Trie:
    def __init__(self):
        self.root=Node()
    def insert(self,val):
        tem=self.root
        for i in val:
            if i not in tem.nod:
                tem.nod[i]=Node()
            tem=tem.nod[i]
    def search(self,val):
        tem=self.root
        for i in val:
            if i not in tem.nod:
                return False
            tem=tem.nod[i]
        return True    
            
            
class Solution:
    def prefixSuffixString(self, s1, s2) -> int:
        #code here
        root1=Trie()
        root2=Trie()
        for word in s1:
            root1.insert(word)
            root2.insert(word[::-1])
        ans=0
        for word in s2:
            if root1.search(word) or root2.search(word[::-1]):
                ans+=1
        return ans
      
"""This code defines a class Node which represents a node in a Trie data structure. Then a class Trie is defined which has a root attribute representing the root node of the Trie. This class has methods insert and search, which are used to insert a word into the Trie and search for a given word, respectively.

The Solution class has a method prefixSuffixString which takes two lists of strings s1 and s2 as input. It first creates two Trie objects root1 and root2. Then it inserts each word in s1 and its reverse into both Tries using the insert method. Finally, it searches for each word in s2 in both Tries using the search method and counts the number of words that are found. This count is returned as the result of the function."""
