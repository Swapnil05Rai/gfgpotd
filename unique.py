
from typing import List


class Solution:
    def uniqueRow(self,row, col, matrix):
    #complete the function
        res_arr=[]
        for rw in matrix:
            if rw not in res_arr:
                res_arr.append(rw)
        return res_arr
