class Solution:
    def findLargest(self, N, S):
        # code here
        x=''
        if S==0 and N==1:
            return 0
        if S==0:
            return -1
        else:
            for i in range(N):
                if S>=9:
                    if i==(N-1) and S>9:
                        return -1
                    S=S-9
                    x+=str(9)
                elif S==0:
                    x+=str(S)
                else:
                    x+=str(S)
                    S=S-S
        return x
