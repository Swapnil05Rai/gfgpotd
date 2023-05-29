
class Solution:
    def CamelCase(self,N,Dictionary,Pattern):
        ans=[]
        for i in Dictionary :
            temp=''
            for j in i:
                if j.isupper():
                    temp+=j
                if temp==Pattern:
                    ans.append(i)
                    break
                
        if ans:return ans
        return [-1]
