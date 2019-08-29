# File Recursion

I created a class File_Paths(object): and initialized it with self.
Then I created a list called 'paths_to_files' to store paths.

For the find_files function, I had to add self to suffix, and path.
I first check the base case of the function - if the file does not
exist within the path, I return a print statement stating an invalid 
path exists. Also, I return True.

I then set files = os.listdir(path) to return a list
(in arbitrary order) containing the names of the entries
in the directory given by path.

A for loop is used to search 'files' listdir above. There is no
limit to the depth of the subdirectories searched. 
Recursion is used to find the files within 'testdir' folder.
If the file endswith(suffix), I append the path to
my path_to_files list.

I then print the file paths with a print_paths function running
a for loop in my paths_to_files list.

##### Time Complexity:

I'm running an iteration through all the directories, searching
a specified file. If the file is not found, I'm using recursion 
to continue searching. The time complexity for this algorithm 
is O(n) and linear.

The space complexity for this algorithm iterates over my 
path_to_files list. 'n' is the length of my path_to_files list
and the space complexity is O(n).
