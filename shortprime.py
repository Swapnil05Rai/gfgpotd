class Solution:
    def __init__(self):
        # Every index of prime stores zero or one
        # If prime[i] is zero means i is not a prime
        # If prime[i] is one means i is a prime
        self.prime=[1 for i in range(10001)]

    def shortestPath(self,num1, num2):
        prime = [1 for i in range(10000)]
        for p in range(2, int(9999 ** 0.5) + 1):
            if prime[p]:
                for i in range(p * p, 10000, p):
                    prime[i] = 0
        q = [(num1, 0)]
        st = {num1}
        while q:
            x, y = q.pop(0)
            if x == num2:
                return y
            for k in range(1, 5):
                for a in range(10):
                    j = 10 ** (4 - k)
                    l = (x // j) % 10
                    if l != a:
                        newl = x + (a - l) * j
                        if newl not in st and prime[newl] and 1000 <= newl < 10000:
                            q.append((newl, y + 1))
                            st.add(newl)
        return -1
      
      
"""The function takes two integer arguments num1 and num2, which represent the starting and ending four-digit prime numbers, respectively. The function returns an integer representing the shortest path from num1 to num2 that can be attained by altering only one single digit at a time. Every number obtained after changing a digit should be a four-digit prime number with no leading zeros.

The function first initializes a list prime of size 10000, where prime[i] is 1 if i is a prime number and 0 otherwise. Then, it uses the Sieve of Eratosthenes to efficiently mark all non-prime numbers in the prime list.

Next, it initializes a queue q with the tuple (num1, 0), where the second element of the tuple represents the distance from num1. It also initializes a set st to store the visited states, and adds num1 to the set.

The function then enters a loop that continues until the queue q is empty. Inside the loop, it retrieves the front element (x, y) from the queue, where x is the current four-digit prime number and y is its distance from num1. If x is equal to num2, the function returns y as the result. Otherwise, it loops through the digits of x and tries all possible values for each digit. For each digit k, it constructs a new four-digit prime number newl by replacing the digit with a new value a. If newl is not in st, is a prime number, has no leading zeros, and is a four-digit number, it adds (newl, y + 1) to the queue and adds newl to the set st. After trying all possible values for each digit, the function increments the distance y by 1 and continues the loop.

If the loop completes and the queue is empty, the function returns -1, indicating that num2 is not reachable from num1."""
