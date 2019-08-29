# File Recursion
'''
Finding Files
For this problem, the goal is to write code for finding all files
under a directory (and all directories beneath it) that end
with ".c"

Here is an example of a test directory listing, which can be
downloaded here:

https://s3.amazonaws.com/udacity-dsand/testdir.zip

./testdir
./testdir/subdir1
./testdir/subdir1/a.c
./testdir/subdir1/a.h
./testdir/subdir2
./testdir/subdir2/.gitkeep
./testdir/subdir3
./testdir/subdir3/subsubdir1
./testdir/subdir3/subsubdir1/b.c
./testdir/subdir3/subsubdir1/b.h
./testdir/subdir4
./testdir/subdir4/.gitkeep
./testdir/subdir5
./testdir/subdir5/a.c
./testdir/subdir5/a.h
./testdir/t1.c
./testdir/t1.h

Python's os module will be useful—in particular,
you may want to use the following resources:

os.path.isdir(path)
    Return True if path is an existing directory. This follows
    symbolic links, so both islink() and isdir() can be true
    for the same path.

os.path.isfile(path)
    Return True if path is an existing regular file. This
    follows symbolic links, so both islink() and isfile()
    can be true for the same path.

os.listdir(directory)
    Return a list containing the names of the entries in the
    directory given by path. The list is in arbitrary order,
    and does not include the special entries '.' and '..' even
    if they are present in the directory.

    path may be a path-like object. If path is of type bytes
    (directly or indirectly through the PathLike interface),
    the filenames returned will also be of type bytes; in all
    other circumstances, they will be of type str.

    This function can also support specifying a file descriptor;
    the file descriptor must refer to a directory.

    *Note To encode str filenames to bytes, use fsencode().
    See also The scandir() function returns directory entries along
    with file attribute information, giving better performance for
    many common use cases.

os.path.join(...)
    Join one or more path components intelligently. The return
    value is the concatenation of path and any members of *paths
    with exactly one directory separator (os.sep) following each
    non-empty part except the last, meaning that the result will
    only end in a separator if the last part is empty.
    If a component is an absolute path, all previous components
    are thrown away and joining continues from the absolute
    path component.

*Note: os.walk() is a handy Python method which can achieve this
task very easily. However, for this problem you are not allowed
to use os.walk().
'''

# OS Module Exploration Code
# Code to demonstrate the use of some of the OS modules in python
import os


class File_Paths(object):
    def __init__(self):
        self.paths_to_files = []

    def find_files(self, suffix, path):
        # Base Case
        if(not(os.path.exists(path))):
            print('Not a valid path. Please check path and try again.')
            return True

        files = os.listdir(path)
        # Find all files beneath path with file name suffix.
        for file in files:
            # No limit to the depth of the subdirectories searched.
            if(os.path.isdir(path + "/" + file)):
                # Recursion
                self.find_files(suffix, path + "/" + file)
            else:
                if(file.endswith(suffix)):
                    self.paths_to_files.append(path + "/" + file)

    # Returns a list of paths
    def print_paths(self):
        if(len(self.paths_to_files) == 0):
            print("File not found.")
            return
        for file in self.paths_to_files:
            print(file)


# Finding all files under a directory (and all directories
# beneath it) that end with ".c"
print("\nFinding all files under a directory(and all subdirectories) \
that end with 'c':")
path_1 = File_Paths()
if(not(path_1.find_files('.c', 'testdir'))):
    path_1.print_paths()

# Locally save a file ex.py
# Checks if this file is indeed a file!
# Does the file end with .py?
print("\nLocally saved a file ex.py and checks if this is a file:")
path_2 = File_Paths()
if(not(path_2.find_files('ex.py', '.'))):
    path_2.print_paths()


print("\nPrint the files in the directory 'testdir' that are running \
this script:")
path_3 = File_Paths()
if(not(path_3.find_files('', 'testdir'))):
    path_3.print_paths()
