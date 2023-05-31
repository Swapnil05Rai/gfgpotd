def LargButMinFreq(arr,n):
    #code here
    m={}
    for i in arr:
        m[i]=m.get(i,0)+1
    v=1e9;ans=0
    for i in m:
        if v>m[i]:
            ans=i
            v=m[i]
        elif v==m[i]:
            ans=max(ans,i)
    return ans
