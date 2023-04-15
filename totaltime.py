 def totalTime(self, n : int, arr : List[int], time : List[int]) -> int:
        m = {}
        cur = -1
        for e in arr:
            cur += 1
            if e not in m:
                m[e] = cur
            else:
                passed = cur - m[e]
                cur += max(0, time[e-1]-passed)
                m[e] = cur
        return cur
      
"""This is a function that calculates the total time required to process a given list of tasks.

The function takes three inputs:

n: an integer representing the number of tasks to be processed
arr: a list of integers representing the task IDs to be processed
time: a list of integers representing the time required to process each task ID
The function initializes an empty dictionary m and a variable cur to -1. It then loops through each task in arr, using cur to keep track of the current time.

If the current task ID e is not in m, it adds it to m with the current index cur.

If e is already in m, it calculates the time that has passed since the last occurrence of e using cur - m[e]. It then adds the maximum of 0 and the difference between time[e-1] (the time required to process e) and passed to cur to represent the time required to process the current task e. It updates m[e] to the new index cur.

Finally, the function returns the value of cur, which represents the total time required to process all the tasks."""
