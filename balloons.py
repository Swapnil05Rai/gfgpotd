def maxInstance(s):
    a = [0, 0, 0, 0, 0]
    for char in s:
        if char == 'b':
            a[0] += 1
        elif char == 'a':
            a[1] += 1
        elif char == 'l':
            a[2] += 1
        elif char == 'o':
            a[3] += 1
        elif char == 'n':
            a[4] += 1
    
    a[2] = a[2] // 2
    a[3] = a[3] // 2
    return min(a)

  
  """An array a of size 5 is initialized with all values set to 0.
  The array a is used to keep count of the number of occurrences of the characters 'b', 'a', 'l', 'o', and 'n' in the input string s.

A loop iterates over the characters in the input string s.
If a character is equal to 'b', 'a', 'l', 'o', or 'n', the corresponding element in the array a is incremented.

The number of 'l' characters in the string is divided by 2 and the number of 'o' characters is also divided by 2.
This is because each instance of the word "balloon" contains two 'l' characters and two 'o' characters.

Finally, the function returns the minimum value in the array a.
This is because the number of instances of the word "balloon" that can be made is limited by the character that occurs the fewest number of times.

So, the code counts the number of occurrences of each character in the word "balloon" in the input string, 
and returns the maximum number of complete instances of the word "balloon" that can be made.




"""
