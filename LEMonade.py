class Solution:
    def lemonadeChange(self, N, bills):
        # Code here
        fnotes,tnotes = 0,0
        for i in bills:
            if i==5:
                fnotes += 1
            elif i==10:
                if not fnotes:
                    return False
                fnotes -= 1
                tnotes += 1
            else:
                if not fnotes:
                    return False
                elif not tnotes:
                    if fnotes < 3:
                        return False
                    fnotes -= 3
                else:
                    fnotes -= 1
                    tnotes -= 1
        return True
