def longestSubsequence(self,a,n):
        # code here
        lis = []          #empty list
        
        for card in a:
            left, right = 0, len(lis) - 1
            while left <= right:
                mid = (left + right) // 2
                if lis[mid] >= card:
                    right = mid - 1
                else:
                    left = mid + 1
            if left == len(lis):
                lis.append(card)
            else:
                lis[left] = card
        
        return len(lis)
