class Solution:
    def appleSequences(self, n: int, m: int, arr: str) -> int:
        maxlen = 0
        end = 0
        start = 0
        count = 0

        while end < n:
            if arr[end] == 'O':
                count += 1

            while start < n and count > m:
                if arr[start] == 'O':
                    count -= 1
                start += 1

            maxlen = max(maxlen, end - start + 1)
            end += 1

        return maxlen

      
      
"""The appleSequences function takes three arguments n, m, and arr which represent the length of the string, the maximum number of 'O's allowed in the subarray, and the string itself.

The function initializes maxlen, end, start, and count to 0.

It then enters a while loop that runs as long as end is less than the length of the string. Inside the loop, it increments count if the character at the current index in the string is 'O'.

If the count is greater than m, the function enters another while loop that runs as long as start is less than the length of the string and the count is greater than m. Inside the inner while loop, the function decrements count if the character at the current index in the string is 'O', and increments start.

Once the count is less than or equal to m, the function calculates the length of the current subarray, updates maxlen if necessary, increments end, and continues the outer while loop until it has processed the entire string.

Finally, the function returns the value of maxlen, which represents the length of the longest subarray of consecutive 'O's that has at most m 'O's."""
