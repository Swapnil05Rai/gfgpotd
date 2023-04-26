def is_possible_to_get_seats(self, n : int, m : int, seats : List[int]) -> bool:
        # code here
        available=1#CoverYourBase
        ans=0
        for i in range(m):
            if seats[i]==0:
                available+=1 
            else:
                ans+=max(0,(available-1)//2)
                available=0
        
        available+=1#ZeroDefence    
        ans+=(available-1)//2
                
        if ans>=n:
            return True
        else:
            return False
          
          
"""This is a function that takes in three parameters: n, m, and seats, where n represents the number of people who want to buy tickets, m represents the number of seats in a row, and seats is a list of integers of length m representing the availability of each seat (1 if it is occupied, 0 if it is available).

The function determines whether it is possible to sell n tickets such that no two people sit next to each other. It does so by iterating through the seats list and counting the number of available seats in between two occupied seats. If this count is greater than or equal to (n-1)//2, where // denotes integer division, then it is possible to sell n tickets without any two people sitting next to each other.

The variable available is initialized to 1 to account for the possibility of a person being able to sit at the very beginning of the row. Then, the function iterates through the seats list and checks if the current seat is available or occupied. If the current seat is available, available is incremented by 1. If the current seat is occupied, the function calculates the number of available seats between the previous occupied seat and the current one, and adds (available-1)//2 to the ans variable. Then, available is set to 0 to start counting available seats from the current position.

After the loop, available is incremented by 1 to account for the possibility of a person being able to sit at the very end of the row. The number of available seats between the last occupied seat and the end of the row is calculated and added to ans. Finally, the function checks whether ans is greater than or equal to n. If it is, the function returns True, indicating that it is possible to sell n tickets without any two people sitting next to each other. If ans is less than n, the function returns False."""
