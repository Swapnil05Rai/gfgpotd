class Solution:
    def minSteps(self, str : str) -> int:
        c=1
        for i in range(1,len(str)):
            if (str[i]!=str[i-1]):
                c+=1
        return (c//2)+1
        
        
"""This code calculates the minimum number of steps required to convert a string to a palindrome, where each step consists of selecting two adjacent characters in the string and replacing them with a character that is the average of the two selected characters (i.e., the character with ASCII value equal to the average of the ASCII values of the selected characters, rounded down to the nearest integer).

The minSteps function takes a single argument str, which is a string. It initializes a variable c to 1, which will count the number of steps required. Then, it loops through each character in the string, starting from the second character (index 1), and checks if the current character is different from the previous character. If it is, it increments c by 1.

After the loop, it calculates the number of pairs of adjacent characters that need to be replaced by dividing c by 2 and adding 1. This is because each pair of adjacent characters requires one step, and the final character in the string does not require any steps.

Finally, the function returns the calculated value."""
