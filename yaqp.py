from typing import List
class Solution:
    def solveQueries(self, N : int, num : int, arr : List[int], Q : List[List[int]]) -> List[int]:
        ans=[]
        freq=[0]*N
        dic={}
        for i in range(N):
            if arr[i] in dic:
                freq[i]=dic[arr[i]]+1
                dic[arr[i]]+=1
            else:
                freq[i]=1
                dic[arr[i]]=1
        for q in Q:
            l=q[0]
            r=q[1]
            k=q[2]
            cnt=0
            vis=[]
            for i in range(l,r+1):
                if arr[i] not in vis and ((dic[arr[i]]-freq[i])+1)==k:
                    cnt+=1
                    vis.append(arr[i])
            ans.append(cnt)
        return ans

"""This is a Python solution to a problem that involves answering queries on a given array. The input consists of an integer N, an integer num, a list arr of length N, and a list of queries Q. Each query is represented as a list of three integers [l, r, k].

The goal is to count the number of elements in arr[l:r+1] that appear exactly k times in the subarray.

The solution works as follows:

Initialize an empty list ans and a list freq of length N filled with zeroes. Initialize an empty dictionary dic.
Iterate over the elements in arr using a loop. For each element, check if it's already in dic. If it is, increment the corresponding value in freq and set freq[i] to dic[arr[i]]+1. If it's not in dic, set freq[i] to 1 and add the element to dic with a value of 1.
Iterate over the queries in Q using a loop. For each query, extract the values l, r, and k.
Initialize a variable cnt to 0 and an empty list vis. Iterate over the subarray arr[l:r+1] using a loop. For each element, check if it's already in vis and if (dic[arr[i]]-freq[i])+1 equals k. If both conditions are true, increment cnt by 1 and add the element to vis.
Append cnt to ans and return ans.
In essence, the solution uses a dictionary to count the frequency of elements in the input array, and then uses that information to answer the queries by iterating over the subarrays and checking if the frequency of each element is equal to the given value k."""
