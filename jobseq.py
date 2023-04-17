def JobScheduling(self,Jobs,n):
        M = max( j.deadline for j in Jobs )
        avail = list(range(M+1))
        cnt, ans = 0, 0
        Jobs.sort(key=lambda x: (-x.profit, x.deadline))
        for job in Jobs:
            dl, prof = job.deadline, job.profit
            par, i = avail[dl], dl
            while i>0 and i!=par:
                avail[i] = avail[par]
                i = par
                par = avail[par]
            if i>0:
                avail[i] = i-1
                cnt += 1
                ans += prof
        
        return cnt, ans
      
"""The given code implements a solution to the Job Scheduling problem, which involves scheduling a set of jobs to be executed on a single machine with limited capacity. The goal is to maximize the total profit earned by completing the jobs before their respective deadlines.

The function takes two inputs:

Jobs: a list of Job objects with attributes deadline (int) and profit (int).
n: the number of jobs in the list.
The function first determines the maximum deadline among all jobs and creates a list of available time slots from 0 to M (inclusive).

Then, it initializes two variables: cnt (count) and ans (answer) to zero.

The list of jobs is sorted in descending order of profit and ascending order of deadline.

Next, the function iterates through the sorted list of jobs. For each job, it retrieves its deadline and profit, and finds the latest available time slot (par) on or before the deadline. It then finds the latest available time slot (i) in the chain of time slots starting from par and working backwards.

If the found time slot i is greater than 0, then the job can be scheduled before its deadline, and the function updates the available time slots list and increments the count and answer variables.

Finally, the function returns the count and the total profit earned by completing the scheduled jobs before their respective deadlines.

In summary, the code implements a greedy algorithm to solve the Job Scheduling problem in O(n^2) time complexity."""
