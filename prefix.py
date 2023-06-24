class Solution:
    def klengthpref(self,arr,n,k,s):
        # return list of words(str) found in the board
        c=0
        l=[]
        c_s=s[0:k]
        for i in range(n):
            l.append(arr[i][0:k])
        # print(c_s)
        # print(l)
        if k>len(s):
            return 0
        else:
            for i in range(n):
                if c_s ==l[i]:
                    c+=1
            return c
