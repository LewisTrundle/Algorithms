"""
Given an 8x8 chess board with each square labelled with the integer 0-63,
this algorithm returns the number of moves it takes for a knight to move between two squares.
Note: this uses a BFS algorithm.
"""

""" Each square on the board has an x and y coordinate and a number of moves from starting position """
class Square:
    def __init__(self, x, y, moves):
        self.x = x
        self.y = y
        self.moves = moves
        
        
""" Gets the coordinates of a square from its integer position """
def get_coord(pos):
    for number in range(8):
        if (pos-number) % 8 == 0:
            y_coord = number
    x_coord = pos // 8
    return (x_coord, y_coord)


""" Returns false if coordinates of possible move is outside chess board """
def check_boundary(x, y):
    if ((x < 0 or x > 7) or (y < 0 or y > 7)):
        return False
    return True
        

def solution(src, dest):
    # Gets the coordinates of the starting and final destination
    src_pos = get_coord(src)
    dest_pos = get_coord(dest)
    
    # Create the chess board and maps every square as False - meaning the square hasn't been tried yet
    board = [[False for i in range(8)] for j in range(8)]
    # Sets the starting position on the board to True
    board[src_pos[0]][src_pos[1]] = True
    
    # These are the coords for all possible moves of a knight - e.g. the first move a knight can do is (1, 2)
    pos_x = [1, -1, 1, -1, 2, -2, 2, -2]
    pos_y = [2, 2, -2, -2, 1, 1, -1, -1]


    # The queue holds each possible square to try
    queue = []
    # Adds the starting square to the queue
    queue.append(Square(src_pos[0], src_pos[1], 0))
    

    # Repeats until all possible moves have been tried
    while (len(queue) > 0):
        # Gets the first square in the queue
        square = queue[0]
        queue.pop(0)
        
        # If the coords of the current square matches the destination, return the no. of moves from starting position
        if (square.x == dest_pos[0] and square.y == dest_pos[1]):
            return square.moves
        
        # There are 8 (max) possible moves a knight can move
        # Each possible move is added to the queue
        for i in range(8):
            # Get coords of possible move
            x = square.x + pos_x[i]
            y = square.y + pos_y[i]
            
            # Checks if the possible move will be within the boundaries of the board
            if (check_boundary(x, y) == False):
                continue
            
            # If the square has not been tried yet, add it to the queue
            if (board[x][y] == False):
                board[x][y] = True
                queue.append(Square(x, y, square.moves+1))

        
distance = solution(23, 5)
print(distance)

distance = solution(0, 1)
print(distance)

distance = solution(19, 36)
print(distance)

distance = solution(0, 63)
print(distance)