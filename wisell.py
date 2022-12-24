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
