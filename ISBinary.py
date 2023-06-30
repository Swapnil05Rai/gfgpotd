class Solution:
	    
	def isDivisible(self, s):
	    odd, even, pos = 0, 0, 0
	    for i in s:
	        if i=="1":
	            if pos%2==0:odd+=1
	            else:even+=1
	        pos+=1
	    return 1 if not abs(odd-even)%3 else 0
