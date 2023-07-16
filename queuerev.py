class Solution:
    #Function to reverse the queue.
    def rev(self, q):
        #add code here
        s = []
        
        while not q.empty():
            s.append(q.get())
        
        while s:
            q.put(s.pop())
        
        return q
