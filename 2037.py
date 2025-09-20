# 2037. Minimum Number of Moves to Seat Everyone

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        moves=0
        while(len(students)!=0):
            if(min(students)!=min(seats)):
                moves+=abs(min(students)-min(seats))
            students.remove(min(students))
            seats.remove(min(seats))
        return moves
