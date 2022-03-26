"""
A maze is represented as a matrix of 0s and 1s, where 0s are passable space and 1s are impassable walls. 
The entrance is at the top left (0,0) and the exit is at the bottom right (w-1,h-1).

This algorithm generates the length of the shortest path from the entrance to the exit.
It allows for 1 wall to be removed during the path finding. 
A BFS is used to find the shortest path.

The path length is the total number of nodes passed through, counting both the entrance and exit nodes. 
- The starting and ending positions are always passable (0). 
- The map will always be solvable, though you may or may not need to remove a wall. 
- The height and width of the map can be from 2 to 20. 
- Moves can only be made in cardinal directions.
- No diagonal moves are allowed.
"""


class Space:
    def __init__(self, x, y, moves, wall_destroyed):
        self.x = x
        self.y = y
        self.moves = moves
        self.wd = wall_destroyed


# If space is outside of boundaries of map - returns true, otherwise returns false
def outside_boundary(x, y, width, height):
    if (x > width) or (y > height) or (x < 0) or (y < 0):
        return True
    return False


# Checks if a space is already in the set and whether it has reached the same position in more or less moves
# If returned True, the space is disregarded
def prev_pos(previous, x, y, wd, moves):
    for space in previous:
        if (space.x == x) and (space.y == y) and (space.wd == wd) and (moves >= space.wd):
            return True
    return False
             


def solution(map):
    width = len(map[0])-1
    height = len(map)-1
    
    # These are the transformations that can be applied to the current position so that is moves in only cardinal directions
    # e.g. the first transformation is to move left, so (-1, 0) is added to the current coordinates
    x_moves = [-1, 0, 1, 0]
    y_moves = [0, 1, 0, -1]
    
    # queue holds every space to be checked
    queue = []
    space = Space(width, height, 1, False)
    queue.append(space)
    # previous holds every space previously visited
    previous = {space}

    while (len(queue) > 0):
        position = queue.pop(0)

        # Returns the number of moves when the coords are (0, 0)
        if (position.x == 0 and position.y == 0):
            return position.moves
        
        # Iterates through each cardinal direction (left, up, right, down)
        for i in range(4):
            x = position.x + x_moves[i]
            y = position.y + y_moves[i]
            wall_destroyed = False
            
            # If the space being checked is outside of the map or has been visited previously (in less moves), it's disregarded
            if (outside_boundary(x, y, width, height)) or \
            (prev_pos(previous, x, y, position.wd, position.moves)):
                continue
        
            # If the space is a wall and the current path hasn't destroyed a wall yet
            if (map[y][x] == 1 and position.wd == False):
                wall_destroyed = True
             
            # If the space is passable and the current path hasn't destroyed a wall yet
            elif (map[y][x] == 0) and (position.wd == False): 
                wall_destroyed = False
              
            # If the space is passable and the current path has destroyed a wall
            elif (map[y][x] == 0) and (position.wd == True):
                wall_destroyed = True
            
            # Otherwise, disregard the new space
            else:
                continue

            # Adds the new space to the queue and to the previous set
            space = Space(x, y, position.moves+1, wall_destroyed)
            queue.append(space)
            previous.add(space)
    
    # If map is unsolvable, return -1       
    return -1
             


answer = solution([[1, 1],
                   [1, 1]])
print(answer)

answer = solution([[0, 1, 1, 0], 
                   [0, 0, 0, 1], 
                   [1, 1, 0, 0], 
                   [1, 1, 1, 0]])
print(answer)

answer = solution([[0, 0, 0, 0, 0, 0], 
                   [1, 1, 1, 1, 1, 0], 
                   [0, 0, 0, 0, 0, 0], 
                   [0, 1, 1, 1, 1, 1], 
                   [0, 1, 1, 1, 1, 1], 
                   [0, 0, 0, 0, 0, 0]])
print(answer)

answer = solution([[0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1],
                   [0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0],
                   [0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0],
                   [0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0],
                   [0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0],
                   [0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0],
                   ])
print(answer)


answer = solution([[0, 1, 1, 0, 1, 1, 1],
           [0, 1, 1, 0, 0, 0, 0],
           [0, 1, 1, 0, 1, 1, 0],
           [0, 0, 1, 0, 0, 1, 0],
           [0, 1, 1, 0, 1, 1, 0],
           [0, 0, 1, 0, 1, 1, 0],
           [1, 0, 0, 0, 1, 1, 0]])

print(answer)