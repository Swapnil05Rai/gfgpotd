class Solution:
    def is_prime(self, p):
        if p <= 1:
            return False
        
        for i in range(2, int(p**0.5) + 1):
            if p % i == 0:
                return False
        return True
    
    def get_nearest_prime(self, num):
        if self.is_prime(num):
            return num
        
        left = num-1
        right = num+1
        
        while left >= 0 and not self.is_prime(left):
            left -= 1
        while not self.is_prime(right):
            right += 1
        
        if left < 0:
            return right
        
        return left if num - left <= right - num else right
    
    def primeList(self, head):
        temp = head
        
        while temp:
            temp.data = self.get_nearest_prime(temp.data)
            temp = temp.next
        return head
"""The code is defining a class called Solution which contains several functions. The main function, primeList, takes a linked list as input, 
where each node of the linked list is an instance of the Node class.
The function modifies the linked list by changing the values stored in each node to the nearest prime number.

The get_nearest_prime function finds the nearest prime number to a given integer num. 
It first checks if num is a prime number using the is_prime function. If num is not a prime, 
the function looks for the nearest prime number by searching in both directions, to the left and to the right of num.
It continues to search in a direction until it finds a prime number,
and then returns the nearest prime number to num based on which direction has a prime number closest to num.

The primeList function iterates through each node of the linked list and calls get_nearest_prime on the value stored in the node. 
The function then updates the value of the node with the result of get_nearest_prime, effectively converting each node's value to the nearest prime number.
The modified linked list is then returned as the result of the primeList function.



"""
