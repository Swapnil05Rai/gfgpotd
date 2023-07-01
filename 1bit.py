class Solution:
	def setBits(self, N):
		# code here
		a=bin(N)
		return (a.count('1'))
