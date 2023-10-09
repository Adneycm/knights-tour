"""
If all squares are visited 
    print the solution
Else
   a) Add one of the next moves to solution vector and recursively 
   check if this move leads to a solution. (A Knight can make maximum 
   eight moves. We choose one of the 8 moves in this step).
   b) If the move chosen in the above step doesn't lead to a solution
   then remove this move from the solution vector and try other 
   alternative moves.
   c) If none of the alternatives work then return false (Returning false 
   will remove the previously added item in recursion and if false is 
   returned by the initial call of recursion then "no solution exists" )
"""

import numpy as np
import random

class KnightsTour:
    def __init__(self, n, x, y):
        self.n = n
        self.x = x
        self.y = y
        self.table = np.zeros((n, n), dtype=int)
        self.table[x, y] = 1
        self.solution = [(self.x, self.y)]

    def possibleMoves(self, position):
        x = position[0]
        y = position[1]
        # Possible movements
        moves = [
            (x+2, y+1),
            (x+2, y-1),
            (x+1, y+2),
            (x+1, y-2),
            (x-1, y+2),
            (x-1, y-2),
            (x-2, y+1),
            (x-2, y-1)
        ]
        random.shuffle(moves)

        # Legal possible movements
        legalMoves = []
        
        i = 0
        for move in moves:
            # 1. Removing moves that go out of the table
            if move[0]>=0 and move[0]<self.n and move[1]>=0 and move[1]<self.n:
                # 2. Removing moves that go to places alredy been
                if self.table[move] == 0:
                    legalMoves.append(i)
            i+=1

        moves = [moves[i] for i in legalMoves]
        return moves

    def tour(self):
        print(self.table)
        # if all squares are visited
        if len(self.solution) == self.n**2:
            print(self.table)
            return True
        
        position = self.solution[-1]
        moves = self.possibleMoves(position)
        if len(moves) == 0:
            return False
        for move in moves:
            self.solution.append(move)
            self.table[move] = len(self.solution)
            if self.tour():
                return True
            else:
                self.solution.pop(-1)
                self.table[move] = 0

        return False


        

k = KnightsTour(5, 0, 0)
if k.tour():
    print("Table completed!")
else:
    print("Table incompleted :(")
        

    




