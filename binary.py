class Solution:
    def precompute(self):
        # This method can be used for any necessary precomputation
        pass

    def solve(self, l: int, r: int) -> int:
        # Initialize a count variable to 0
        cnt = 0

        # Iterate through the possible positions of the first set bit
        for i in range(63):
            # If the number with a single set bit at this position is already
            # greater than the upper bound of the range, we can break out of the loop
            if (1 << i) > r:
                break

            # Iterate through the possible positions of the second set bit
            for j in range(i + 1, 63):
                # If the number with two set bits, one at the current position
                # of the first set bit and one at the current position of the
                # second set bit, is already greater than the upper bound of
                # the range, we can break out of the loop
                if (1 << j) > r:
                    break

                # Iterate through the possible positions of the third set bit
                for k in range(j + 1, 63):
                    # If the number with three set bits, one at the current
                    # position of the first set bit, one at the current position
                    # of the second set bit, and one at the current position of
                    # the third set bit, is already greater than the upper bound
                    # of the range, we can break out of the loop
                    if (1 << k) > r:
                        break

                    # Construct the number with three set bits at the current
                    # positions of the first, second, and third set bits
                    n = 0
                    n = n | (1 << i) | (1 << j) | (1 << k)

                    # If the number is within the range, increment the count
                    if n >= l and n <= r:
                        cnt += 1
                    # If the number is greater than the upper bound of the range,
                    # we can break out of the loop
                    elif n > r:
                        break

        # Return the count
        return cnt
