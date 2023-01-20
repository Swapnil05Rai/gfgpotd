class Solution():
    def maxWeightCell(self,N, Edge):
        weight = [0] * N
        for i in range(N):
            if Edge[i] != -1:
                weight[Edge[i]] += i
        max_weight = weight[0]
        max_index = 0
        for i in range(1, N):
            if weight[i] > max_weight:
                max_weight = weight[i]
                max_index = i
        return max_index
 
"""The problem is to find the cell with the maximum weight, which is the sum of cell indexes of all cells pointing to it,
given an array Edge[] of N integers where Edge[i] contains the cell index that can be reached from cell i in one step.
To solve this, we can use two arrays: one to store the weight of each cell, and another to keep track of the maximum weight and the corresponding cell index.
We iterate through the Edge[] array, for each cell i,
we check if the value of Edge[i] is not -1 and if it's not we increment the weight of cell Edge[i] by adding i to it.
Then we initialize two variables: max_weight and max_index, with the first element's weight and index of the weight array,
respectively. We then iterate through the weight array, for each cell i, we check if the weight of the ith cell is greater than max_weight.
If it is, we update max_weight and max_index with the weight of the ith cell and its index, respectively. Finally, we return max_index as the result,
which is the index of the cell with the maximum weight.
"""
