def secondSmallest(self, s, D):
        num = [None]*D
        for i in range(D-1, 0, -1):
            d = min(s-1, 9)
            num[i] = d
            s -= d
        if s > 9:
            return "-1"
        num[0] = s
        
        i = D-1
        while i > 0:
            if num[i] != 0 and num[i-1] != 9:
                num[i] -= 1
                num[i-1] += 1
                return "".join(str(x) for x in num)
            i -= 1
        return "-1"
 

"""This Python function constructs a list num with D-1 elements containing the largest possible digits that sum up to s-1. If the sum of num is greater than s-1 or D is greater than s, the function returns "-1". Otherwise, it adds the remaining digit s-sum(num) to the beginning of num. Finally, it adjusts the digits in num to get the second smallest number and returns it as a string, or returns "-1" if no such number can be obtained."""
