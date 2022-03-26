""" To find the max-flow rate of a graph, the Ford-Fulkerson algorithm can be used.
This has 3 steps...
1) find an augmenting path
2) compute the bottleneck capacity
3) update the augmented and residual graph

Specifically, the Edmonds-Karp version can be used.
This uses a BFS algorithm to repeatedly find the shortest augmenting path """ 


# Used a BFS algorithm to find a path from the current entrance to any reachable exit
def find_path(entrances, exits, path, pathway):
    # Visited makes sure each room is only visited once
    visited = [False] * len(path)
    visited[entrances] = True
    queue = [entrances]
    
    while len(queue) > 0:
        # Loops through the current room in path
        # If it is possible to reach another room from the current room (i.e. the other room has not been visited and the path is > 0) 
        # then visit that room next by adding to queue
        room = queue.pop(0)
        for index, val in enumerate(path[room]):
            if visited[index] == False and val > 0:
                queue.append(index)
                visited[index] = True
                pathway[index] = room
    
    # If an exit has been visited, return True, else return False 
    for e in exits:
        if visited[e] == True:
            return True
    return False
    

def solution(entrances, exits, path):
    max_flow = 0
    e = 0          # e is used to switch between every entrance after each iteration of the while loop
    pathway = [-1] * len(path)  # keeps track of which rooms where visited

    # Loop repeats while there is a path from the current entrance to any of the exits
    while find_path(entrances[e], exits, path, pathway):
        entrance = entrances[e]
        flow = float("inf")
         
        # Gets the first exit which was reached when the most recent path was found
        for x in exits:
            if pathway[x] != -1:
                ex = x
                cur_room = x
                break
            
        # Gets the bottleneck value of the current path
        while(ex != entrance):
            flow = min(flow, path[pathway[ex]][ex])
            ex = pathway[ex]
             
        max_flow += flow
        
        # Updates both the augmented and residual graph            
        while(cur_room != entrance):
            prev_room = pathway[cur_room]
            path[prev_room][cur_room] -= flow   # residual
            path[cur_room][prev_room] += flow   # augmented
            cur_room = pathway[cur_room]
        
        # Gets the next entrance
        if e >= len(entrances)-1:
            e = 0
        else:
            e += 1
        
        # Re-initialises pathway
        pathway = [-1] * len(path)

    return max_flow

answer = solution([0], [3], 
                  [[0, 7, 0, 0], 
                   [0, 0, 6, 0],
                   [0, 0, 0, 8],
                   [9, 0, 0, 0]])   # 6
print(answer, "\n\n")

answer = solution([0], [5], 
                  [[0, 16, 13, 0, 0, 0],
                   [0, 0, 10, 12, 0, 0],
                   [0, 4, 0, 0, 14, 0],
                   [0, 0, 9, 0, 0, 20],
                   [0, 0, 0, 7, 0, 4],
                   [0, 0, 0, 0, 0, 0]]) # 23
print(answer, "\n\n")

answer = solution([0, 1], [4, 5], 
                  [[0, 0, 4, 6, 0, 0], 
                   [0, 0, 5, 2, 0, 0], 
                   [0, 0, 0, 0, 4, 4], 
                   [0, 0, 0, 0, 6, 6], 
                   [0, 0, 0, 0, 0, 0], 
                   [0, 0, 0, 0, 0, 0]]) # 16
    
print(answer)