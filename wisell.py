class Solution:
    def wineSelling(self, arr, N):
        sum = 0
        i = 0
        j = 0
        while i < N and j < N:
            if arr[i] == 0 or arr[i] < 0:
                i += 1
                continue
            if arr[i] > 0:
                while arr[j] >= 0 and j < N:
                    j += 1
                ele1 = arr[i] * 1
                ele2 = abs(arr[j]) * 1
                dist = abs(i - j) * 1
                mul1 = ele1 * dist
                mul2 = ele2 * dist
                if mul1 > mul2:
                    sum += mul2
                    arr[i] = ele1 - ele2
                    arr[j] = 0
                else:
                    sum += mul1
                    arr[i] = 0
                    arr[j] = ele1 - ele2
        return sum

    
    """Initialize two variables i and j to 0. These variables will be used to iterate over the houses.
Start a while loop that will run until either i or j becomes greater than or equal to N.
Inside the loop, check if the current house at index i has a demand of 0 or if it is a selling house (has a negative demand). If either of these conditions is true, increment i by 1 and continue to the next iteration of the loop.
If the current house at index i has a positive demand, start another loop that will run until either j becomes greater than or equal to N or the current house at index j becomes a buying house (has a negative demand). Inside this loop, increment j by 1 on each iteration.
Once the inner loop is finished, calculate the distance between the current house at index i and the buying house at index j as dist = abs(i - j).
Calculate the amount of wine that the current house at index i is demanding as ele1 = arr[i] * 1. Calculate the amount of wine that the buying house at index j is willing to buy as ele2 = abs(arr[j]) * 1.
Calculate the total work required to transfer the wine from the buying house at index j to the current house at index i as mul1 = ele1 * dist. Calculate the total work required to transfer the wine from the current house at index i to the buying house at index j as mul2 = ele2 * dist.
Compare mul1 and mul2 and choose the minimum value. Update the demand of the current house at index i and the buying house at index j accordingly. Add the minimum value to the sum variable.
Repeat the loop until i or j becomes greater than or equal to N.
Return the sum variable as the result."""
