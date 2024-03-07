"""
   This exercise asks students to write a recursive program to visit
   a Unix direcory tree recursively starting from a giving directory. Print
   only the file name when visiting.

   Students are not allowed to use the os.walk() method, which
   basically does the recursion.

"""

import os, sys


def list_dir(start_dir):
    """
        list_dir lists the contents of a starting directory
        and the contents of all its subdirectories recursively.

        Input:
        start_dir - name of the starting directory
        Output: a complete list of contents of all subdirectories
    """

    # Set the starting directory and retrieve its contents
    path = start_dir

    # Check if a path is not a directory i.e. it is a file, print the path
    if not os.path.isdir(path):
        print(path)
    else:
        # Print the contents in this directory recursively
        for f in os.listdir(path):
            # Convert it into a complete path, needed for 'isdir()'
            # 'v' will be needed to run 'isdir()' when recursive call is made
            v = os.path.join(path, f)
            print(f, v)

    ## Student need to fill in the rest of the method
    ## to accomplish the task specified in the lab description
