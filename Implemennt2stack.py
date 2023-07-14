class TwoStacks:
    def __init__(self, n=100):
        self.size = n
        self.arr = [0] * n
        self.top1 = -1
        self.top2 = n
        self.arr[0] = []
        self.arr[1] = []
        # print(self.arr)
 
    # Function to push an integer into stack 1
    def push1(self, x):
        self.arr[0].append(x)
        
        
    # Function to push an integer into stack 2
    def push2(self, x):
        self.arr[1].append(x)
        
        
    # Function to remove an element from top of stack 1
    def pop1(self):
        if len(self.arr[0]) > 0:
            p = self.arr[0].pop()
            return p
        else:
            return -1
        
        
    # Function to remove an element from top of stack 2
    def pop2(self):
        if len(self.arr[1]) > 0:
            p = self.arr[1].pop()
            return p
        else:
            return -1
