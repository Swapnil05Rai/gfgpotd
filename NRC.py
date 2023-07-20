def nonrepeatingCharacter(self,s):
        d={}
        if len(s)==0:
            return '$'
        for i in s:
            d[i]=1+d.get(i,0)

        for c in s:
            if d[c]==1:
                return c
       
               
        return '$'
