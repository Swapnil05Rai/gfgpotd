def findTriplets(self, arr, n):
        #code here
        arr.sort()
        for i in range(n):
            sum = 0-arr[i]
            j = i+1
            k = n-1
            while(j<k):
                if(arr[j]+arr[k] == sum):
                    return 1
                elif(arr[j]+arr[k] > sum):
                    k-=1
                else:
                    j+=1
        return 0 
