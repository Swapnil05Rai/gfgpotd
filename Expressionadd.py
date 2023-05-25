class Solution:
    def addOperators(self, S, target):
        result = []
        self.addOperatorsHelper(S, target, '', 0, 0, result)
        return result
    
    def addOperatorsHelper(self, num, target, expr, cur_val, prev_num, result):
        if not num and cur_val == target:
            result.append(expr)
            return

        for i in range(1, len(num) + 1):
            curr_str = num[:i]
            if len(curr_str) > 1 and curr_str[0] == '0':
                # Ignore numbers with leading zeros
                continue

            curr_num = int(curr_str)
            next_num = num[i:]

            if not expr:
                # Start of the expression
                self.addOperatorsHelper(next_num, target, curr_str, curr_num, curr_num, result)
            else:
                # Try addition
                self.addOperatorsHelper(next_num, target, expr + '+' + curr_str, cur_val + curr_num, curr_num, result)

                # Try subtraction
                self.addOperatorsHelper(next_num, target, expr + '-' + curr_str, cur_val - curr_num, -curr_num, result)

                # Try multiplication
                self.addOperatorsHelper(next_num, target, expr + '*' + curr_str, cur_val - prev_num + prev_num * curr_num, prev_num * curr_num, result)
