"""
Numbers are stacked in a triangular shape, starting from the corner, for example:

| 7
| 4 8
| 2 5 9
| 1 3 6 10

Each number can be represented as a coord (x, y), with x being the distance 
from the vertical wall, and y being the height from the ground.
For example, 1 is at coord (1, 1) and 9 is at (3, 2).

This algorithm returns the number at a given coord (x, y). 
Each value of x and y must be at least 1 and no greater than 100,000. 
As the numbers can be very large, the answer is returned as a string representation of the number.
"""

""" The ID is equal to the sum of consecutive integers from 1 to x, plus the sum of consecutive integers from x to (x+y-2)
This can be simplified to just the sum of numbers from 1 to (x+y-2) then + x """


def solution(x, y):
    #row = sum(range(1, x+1))
    #add = sum(range(x, (x+y)-1))
    id_no = sum(range(1, (x+y-1))) + x
    return(str(id_no))
    
    
ID = solution(3, 2)     # should print 9
print(ID)

ID = solution(5, 10)    # should print 96
print(ID)