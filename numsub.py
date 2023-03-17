class Solution():
    def no_of_subarrays(self, n,arr):
        last=-1
        cur=-1
        result=0
        for i in range(n):
            if arr[i]==1 and last!=-1:
                diff=cur-last+1
                result+=diff*(diff+1)//2
                cur=-1
                last=-1
            elif arr[i]==0:
                if last==-1:
                    last=i
                    cur=i
                else:
                    cur=i
        if last!=-1:
            diff=cur-last+1
            result+=diff*(diff+1)//2
        return result
      
"""This is a Python code implementation of a function called no_of_subarrays inside a class named Solution. The function takes two arguments, n and arr, where n represents the length of the input array arr and arr represents an array of binary integers (either 0 or 1).

The purpose of this function is to count the number of subarrays in arr that have all 1s in them.

The code uses two variables, last and cur, to keep track of the indices of the last and current occurrence of 1 in the input array arr. It also uses a variable result to keep track of the count of subarrays with all 1s.

The code iterates through the input array arr using a for-loop. If the current element is 1 and there was a previous occurrence of 1, the code calculates the difference between the current and last indices and adds the number of subarrays with all 1s in that range to the result variable using the formula (diff*(diff+1)//2). It then resets the last and cur variables to -1, indicating that there are no more consecutive 1s in the input array.

If the current element is 0, the code updates the last and cur variables to the current index if there was no previous occurrence of 1, or updates only the cur variable if there was a previous occurrence of 1.

After iterating through the entire input array arr, if there was a previous occurrence of 1 (i.e., the last variable is not equal to -1), the code calculates the difference between the current index and the last index and adds the number of subarrays with all 1s in that range to the result variable using the same formula as before.

Finally, the function returns the result variable, which represents the total number of subarrays with all 1s in the input array arr."""
