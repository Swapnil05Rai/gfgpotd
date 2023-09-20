def rotate(self, N, D):
        # code here
        if D>16:
            D = D%16
            
        binary = str(bin(N)[2:])
        ln = len(binary)
        dif = 16-ln
        zero = '0'*dif
        new_binary = zero+binary
        # print(new_binary)
        ans = []
        # left
        e_l = new_binary[:D]
        left = new_binary[D:]+e_l
        ans.append(int(left,2))
        
        # right
        e_r = new_binary[16-D:]
        right = e_r+new_binary[:16-D]
        ans.append(int(right,2))

        return ans
