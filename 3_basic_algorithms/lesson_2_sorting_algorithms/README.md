# Most Common Sorting Algorithms

##### Bubble Sort Efficiency
	O(n^2)

##### Efficiency of Merge Sort
The efficiency of the merge sort algorithm is
	O(#comparisons per step * #steps)
	O(n x log[base2](n))

The efficiency of merge sort is better than the
efficiency of bubble sort.

However, the space efficiency of merge sort is
actually worse than bubble sort. In bubble sort,
we were sorting in place. Basically, we didn't
use extra arrays.

Auxillary Space = O(n)


##### Quicksort
In many cases, quicksort is one of the most
efficient sorting algorithms.

The efficiency of quicksort is actually pretty
complicated. The magic is that it cuts the number
of comparisons needed by splitting the array in half.

The worst case of quicksort O(n^2). That's a really
terrible efficiency.

The average and best-case complexity are actually
O(n(log(n))). Pick a random number, move it close to the 
middle, and split the array in half every time.

Space is O(1)



