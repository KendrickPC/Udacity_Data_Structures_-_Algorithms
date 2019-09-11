import heapq
import math
from helpers import Map, load_map, show_map


def shortest_path(M, start, goal):
    frontier = [(0, start)]
    derived_from = {}
    derived_from[start] = None
    sum_cost = {}
    sum_cost[start] = 0

    while len(frontier) > 0:
        node = heapq.heappop(frontier)[1]

        # Base Case testing of start and goal being at the same place.
        if node == goal:
            break

        # roads is initialized in the Map class from helpers.py file
        for next_node in M.roads[node]:
            # Calculating the cost and distance taken from chosen path.
            # intersections initialized in Map class from helpers.py
            cost_of_path = distance(M.intersections[node], M.intersections[next_node])
            updated_cost = sum_cost[node] + cost_of_path

            if next_node not in sum_cost or updated_cost < sum_cost[next_node]:
                derived_from[next_node] = node
                sum_cost[next_node] = updated_cost
                heapq.heappush(frontier, (updated_cost, next_node))

    return best_route(derived_from, start, goal)


# math.hypot
# https://docs.python.org/2/library/math.html
def distance(start, end):
    # Return the Euclidean norm, sqrt(x*x + y*y).
    # This is the length of the vector from the origin to point (x, y).
    return math.hypot(end[0] - start[0], end[1] - start[1])


def best_route(derived_from, start, goal):
    node = goal
    path = []

    # Base Case for Node not found 
    if node not in derived_from:
        print("Node: {} not found.".format(node))
        return

    while node != start:
        path.append(node)
        node = derived_from[node]
        

    path.append(start)
    path.reverse()
    print(path)
    return path



'''
Resources for A*:

https://www.redblobgames.com/pathfinding/a-star/implementation.html#python
https://www.laurentluce.com/posts/solving-mazes-using-python-simple-recursivity-and-a-search/
http://theory.stanford.edu/~amitp/GameProgramming/AStarComparison.html
https://www.youtube.com/watch?v=ob4faIum4kQ
https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2
'''
