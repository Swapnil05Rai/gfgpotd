class Solution:

	def count(self,arr, n, x):
	    count=0
		for a in range(n):
		    if arr[a]==x:
		        count+=1
		return count
