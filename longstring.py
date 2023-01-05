class Solution():

    def longestString(self, arr, n):

         #your code goes here

        arr.sort()

        max=""

        dict={}

        dict[""]=1

        for i in range(n):

            if arr[i][:-1] in dict:

                dict[arr[i]]=1

                if len(max)<len(arr[i]):

                    max=arr[i]

        return max
      
      
"""It sorts the array in lexicographic order.
It creates an empty string max to store the result and a dictionary dict to store the strings that are present in the array.
It initializes the dictionary with an empty string as a key. This is because all prefixes of a string are also prefixes of the empty string.
It iterates through the sorted array and for each string it checks if its prefix (excluding the last character) is present in the dictionary. If it is, it adds the string to the dictionary and updates max if the string is longer than the current value of max.
At the end, it returns max which is the longest string that satisfies the condition."""
