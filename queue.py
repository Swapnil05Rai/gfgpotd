#User function Template for python3
class Solution:
    # Function to insert element into the queue
    def insert(self, q, k): 
       q.append(k)
    def findFrequency(self, q, k):
            return q.count(k)
