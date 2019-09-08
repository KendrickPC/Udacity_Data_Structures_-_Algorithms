# Searching in a Rotate Sorted Array

### Explanation
Divide and Conquer technique

Recursive search.




#### Algorithm Time Complexity

#### Algorithm Space Complexity



Problem 2
The principle employed in this algorithms is based directly in the binary search algorithms, differently, to this implementations, in its structure, it has been decided to be employed a more divide approach, rather than computationally expensive on previous levels to spare some division; e.g. when the lists are of size 2, both values could have been checked (though this would have increased our time complexity).

Time and Space complexity
The time complexity being an algorithm based on binary search is O(log(n)). The number of iterations we perform, i.e. recursive depth, follows the rule of recursive_depth^2 = n. Thus if we isolate the number of iterations in relation to the input space (n), we obtain log(n) = recursive_depth. As for the space complexity, it is independent of the input, requiring solely pointers to different array locations; O(1).



The program akes O(log(n)) as it implements a varied form of binary search and length of list halves at every stage, n is the length of list.

Space complexity is O(1) since it is an in place search.