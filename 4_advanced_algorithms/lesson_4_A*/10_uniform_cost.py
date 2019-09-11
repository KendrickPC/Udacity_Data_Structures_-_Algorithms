'''
Uniform Cost search - expands out equally in all directions, may expend
                      additional effort getting to a fairly direct path
                      to the goal.

Greedy best-first search - expands outward toward locations estimated as
                           closer to the goal. If a direct path is available,
                           expends much less effort than Uniform Cost; however,
                           it does not consider any routes in which it may need
                           to temporarily take a further away path in order to
                           arrive at an overall shorter path.

A* Search - utilizes both of these - will try to optimize with both the shortest
            path and the goal in mind. We'll see how this works in the next video.
'''
