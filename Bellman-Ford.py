""" 
The Bellman-Ford algorithm can be used to find the shortest path through all nodes in a 
weighted graph with negative weights 
There are 3 steps: 
1)  Set the distance from the source node to every other node as infinity
        - set the distance from the source node to itself to be 0
        - store this all in a 'distance' array
2)  Iterate N-1 times through the graph and 'relax' each edge
        - in each iteration, every edge should be looped through to 'relax' the path lengths
        - relaxing means a shorter distance from one node to another is found in each iteration
        - update the distance array accordingly 
        - loop should repeat (N-1)(E) times 
3)  Repeat the same as above - i.e iterate through the graph N-1 times and loop through every edge.
    This is done to detect negative-loop cycles
        - if a distance is shortened even further then it must be part of a negative-loop cycle
        - therefore, instead of shortening its distance, we update the distance to negative-infinity 
"""        

def bellman_ford(start, n, times):
    distance = [float("inf")] * n
    distance[start] = 0

    for i in range(0, n-1):
        update = False
        for cur_node in range(0, n):
            for next_node, edge in enumerate(times[cur_node]):
                if edge != 0 and distance[cur_node] + edge < distance[next_node]:
                    distance[next_node] = distance[cur_node] + edge
                    update = True
        if not update:
            break

    for cur_node in range(0, n):
        for next_node, edge in enumerate(times[cur_node]):
            if edge != 0 and distance[cur_node] + edge < distance[next_node]:
                distance[next_node] = float("-inf")
                return distance
    
    return distance

def solution(times):
    n = len(times)
    distances = []

    for i in range(0, n):
        distance = bellman_ford(i, n, times)
        distances.append(distance)

    return distances

answer = solution([[0, 1, 0, 0, 0, 0, 0, 0],
                   [0, 0, 1, 0, 0, 4, 4, 0],
                   [0, 0, 0, 0, 1, 0, 0, 0],
                   [0, 0, 1, 0, 0, 0, 0, 0],
                   [0, 0, 0, -3, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 5, 3],
                   [0, 0, 0, 0, 0, 0, 0, 4],
                   [0, 0, 0, 0, 0, 0, 0, 0]])
print(answer)

answer = solution([[0, 5, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 20, 0, 0, 30, 60, 0, 0, 0],
                   [0, 0, 0, 10, 75, 0, 0, 0, 0, 0],
                   [0, 0, -15, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 100],
                   [0, 0, 0, 0, 25, 0, 5, 0, 50, 0],
                   [0, 0, 0, 0, 0, 0, 0, -50, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, -10, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
print(answer)

answer = solution([[0, 2, 2, 2, -1], 
                   [9, 0, 2, 2, -1], 
                   [9, 3, 0, 2, -1], 
                   [9, 3, 2, 0, -1], 
                   [9, 3, 2, 2, 0]])    
print(answer)

answer = solution([[0, 1, 1, 1, 1], 
                   [1, 0, 1, 1, 1], 
                   [1, 1, 0, 1, 1], 
                   [1, 1, 1, 0, 1], 
                   [1, 1, 1, 1, 0]])    
print(answer)

answer = solution([[0, 1],
                   [1, 0]])      
print(answer)