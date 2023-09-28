def convertToWave(self, n : int, a : List[int]) -> None:
        for i in range(1,n,2):
            temp=a[i-1]
            a[i-1]=a[i]
            a[i]=temp
        return a
