class Solution:
    def asteroidCollision(self, N, asteroids):
        result = []
        for asteroid in asteroids:
            if not result or asteroid > 0:
                result.append(asteroid)
            else:
                while result and result[-1] > 0 and result[-1] < abs(asteroid):
                    result.pop()
                if not result or result[-1] < 0:
                    result.append(asteroid)
                elif result[-1] == abs(asteroid):
                    result.pop()
        return result
      
      
      
     ''' The first line initializes an empty result array to store the surviving asteroids.
The second line begins a loop to iterate through the asteroids array. The loop variable asteroid is set to each element of the array in turn.
The third line is an if statement that checks if the result array is empty or if the current asteroid is moving to the right (has a positive value). If either of these conditions is true, then the current asteroid is added to the result array.
If the if statement is not true, then the else block is executed. The else block begins with another while loop that will continue to execute as long as the result array is not empty, the last asteroid in the result array is moving to the right (has a positive value), and the last asteroid in the result array is smaller than the current asteroid. Inside the while loop, we remove the last asteroid from the result array using result.pop().
After the while loop finishes executing (either because the result array is empty, the last asteroid in the result array is moving to the left, or the last asteroid in the result array is equal to or larger than the current asteroid), the next if statement is executed. This if statement checks if the result array is empty or if the last asteroid in the result array is moving to the left. If either of these conditions is true, then the current asteroid is added to the result array.
If the if statement is not true, then the elif block is executed. This block checks if the last asteroid in the result array is equal in size to the current asteroid. If it is, then both asteroids are removed from the result array using result.pop().
After the loop finishes executing, the result array is returned.'''
