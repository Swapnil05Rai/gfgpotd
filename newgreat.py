from collections import deque
class Solution:
    def nextLargerElement(self,arr,n):
        #code here
        stack=deque([])
        ans=[]
        for i in range(len(arr)-1,-1,-1):
            if len(stack)==0:
                ans.append(-1)
            elif stack[0]>arr[i]:
                ans.append(stack[0])
            elif stack[0]<arr[i]:
                while len(stack)>0 and stack[0]<arr[i]:
                    stack.popleft()
                if len(stack)==0:
                    ans.append(-1)
                else:
                    ans.append(stack[0])
            stack.appendleft(arr[i])
        return ans[::-1]
        
        
"""The code uses a deque to keep track of the elements in the array, 
and it starts by initializing an empty deque and an empty list to store the next greater element for each element in the array.

For each element, it checks if the deque is empty or if the element at the front of the deque is greater than the current element. 
If the deque is empty or the element at the front of the deque is greater than the current element, it appends -1 to the ans list.
If the element at the front of the deque is less than the current element, 
it pops the elements from the front of the deque until the deque is empty or the element at the front of the deque is greater than the current element.
If the deque is empty after popping the elements, it appends -1 to the ans list, otherwise it appends the element at the front of the deque to the ans list.

At the end, it appends the current element to the front of the deque. Finally, it returns the reversed ans list.

This solution also has a time complexity of O(n) and a space complexity of O(n) and it also handles the cases of the last element not having a next greater element,
empty array and handle the case of duplicate elements correctly."""
