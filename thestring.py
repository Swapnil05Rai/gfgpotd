def removePair(s: str) -> str:
    st1, st2 = [], []
    for ch in s:
        st1.append(ch)
    while st1:
        if not st2:
            st2.append(st1.pop())
        elif st1[-1] == st2[-1]:
            st2.pop()
            st1.pop()
        else:
            st2.append(st1.pop())
    ans = ''.join(reversed(st2)) if st2 else "-1"
    return ans
"""This function uses two lists, st1 and st2, to simulate the behavior of stacks.
It iterates through the characters in the input string, and pushes them onto the st1 stack. 
Then, while st1 is not empty, it pops characters from st1 and pushes them onto st2.
If the top character of st1 is the same as the top character of st2, both characters are popped.
Otherwise, the character is pushed onto st2. After all characters have been processed, if st2 is empty, the function returns "-1". 
Otherwise, it returns the reversed contents of st2 as a single string."""
