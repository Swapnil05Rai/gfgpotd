class Solution:
    def xmod11(self,x):
        s = 0 
        for i in range(len(x)):
            if i%2 == 0: 
                s+=int(x[i])*-1
            else: 
                s+=int(x[i])*1
        return s%11
      
"""This is a Python function that computes the check digit of an ISBN-10 number. An ISBN-10 number is a unique identifier assigned to books and consists of 10 digits. The last digit of the ISBN-10 number is called the check digit and is used to verify that the ISBN-10 number is valid.

The function takes in a string x, which represents the ISBN-10 number, and computes the check digit using the following algorithm:

Starting from the leftmost digit, multiply the first digit by -1, the second digit by 1, the third digit by -1, and so on.
Sum the products from step 1.
Take the sum from step 2 modulo 11.
The resulting value is the check digit. The function returns this check digit as an integer.

Note that this function assumes that the input x is a valid ISBN-10 number and does not perform any error checking.



"""
