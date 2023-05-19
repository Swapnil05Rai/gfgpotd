from typing import List
from bisect import bisect_left
class Solution:
    def kthSmallestNum(self, n : int, ranges : List[List[int]], q : int, queries : List[int]) -> List[int]:
        # code here
        ranges.sort()
        ans=[ranges[0]]
        for i in range(1,n):
            if ans[-1][1]>=ranges[i][0]:
                ans[-1][1]=max(ans[-1][1],ranges[i][1])
            else:
                ans.append(ranges[i])
        m=len(ans)
        s=[0]*m
        s[0]=ans[0][1]-ans[0][0]+1
        for i in range(1,m):
            s[i]+=(s[i-1]+ans[i][1]-ans[i][0]+1)
        fans=[]
        for qq in queries:
            i=bisect_left(s,qq)
            if i==m:
                fans+=[-1]
            else:
                ss=0
                if i>0:
                    ss=s[i-1]
                d=s[i]-qq
                fans+=[ans[i][1]-d]
        return fans
#time complexity O(nlog(n)+qlog(n))
#binarysearch


"""This code defines a function kthSmallestNum that takes several inputs: n, ranges, q, and queries. Here, n represents the number of ranges, ranges is a list of ranges represented by pairs of integers, q represents the number of queries, and queries is a list of integers representing the queries.

The function first sorts the ranges list based on the starting values of the ranges. It then merges overlapping ranges and stores the merged ranges in the ans list. Each range in ans represents a non-overlapping range.

Next, it calculates the cumulative sum of the range sizes in the s list. The s list stores the cumulative sizes of the merged ranges. Each element in s represents the sum of the sizes of the ranges up to that index.

After preparing the necessary data structures, the function proceeds to process each query in the queries list. For each query qq, it performs a binary search on the s list to find the index i such that s[i] is the smallest element greater than or equal to qq. If i is equal to the length of s, it means that there are no ranges satisfying the query, so -1 is appended to the fans list. Otherwise, the function calculates the range size difference d by subtracting qq from s[i]. The answer for the query is then determined by subtracting d from the ending value of the range at index i in the ans list, and the result is appended to the fans list.

Finally, the function returns the fans list, which contains the answers to the queries.

In summary, this function merges overlapping ranges, calculates the cumulative sizes of the merged ranges, and efficiently answers queries regarding the k-th smallest number within the ranges.

"""
