Lab Instructions can also be found here:
[https://github.com/fuchsberger/csci204-lab-recursion](https://github.com/fuchsberger/csci204-lab-recursion)

# CSCI 204 Lab: Recursion & File Systems
Lab content is the result of collective work of CSCI 204 instructors.

## Objectives
In this lab, you will implement recursive directory listing on the UNIX file system and handle exceptions.

_We strongly recommend to do this lab on either the linux lab computers or windows computers with WSL installed. Macbooks may also work fine. We do not recommend using your Windows computers (without WSL) as some of the linux commands featured will not work._

**Partner Status:** This lab can be done with a partner, provided that they are in your lab section.  If you work with a partner, follow the same process as previously specified, with one student creating a group and the other joining. Let your lab instructor know if you have any replit issues.

## Directory Structure
Clone this reposity to get a copy of the starting files:
```bash
git clone https://github.com/fuchsberger/csci204-lab-recursion.git
```

Your newly created `csci204-lab-recursion` folder should contain the following files and subfolders:
```bash
README.md
main.py
lab/
  dirs.py
  file1.txt
  file2.txt
  file3.txt
  file4.txt
  testpages/
    level2/
      page1.html
      page2.html
    grading.html
    index.html
    readme.txt
    test.html
    test2.html
```
_Note:_ You may see additional files depending on your operating system and code editor.

`file<1-4>.txt` may help you practice the Linux diff command as described below.

**For the following excercises make sure to navigate to the `/labs` folder in your shell first.**

### Linux command `diff`
Linux provides many useful commands for programmers. The command `diff` is one such command. The `diff` command compares two text files and prints out the differences between the two. It can be used in many ways. For example, you can use the command to see if the output of your program is the same, or very similar to the required output. Please read the following blog post to understand the general meaning of diff output.

https://unix.stackexchange.com/questions/81998/understanding-of-diff-output

After reading the post, try the diff command among the four text files you just copied.
For example:
```
diff file1.txt file2.txt
diff file1.txt file3.txt
diff file2.txt file4.txt
```

Make sure you can explain the output of these comparisons.  You might find it helpful to open the text files to see what's going on.  In the shell, you can, e.g., type `cat file1.txt`

## Recursively Listing Files

### Familiarizing yourself with `dirs.py`
Recursive algorithms are natural for solutions to problems with hierarchical structure. An example problem is listing all the files in a directory and all of its sub-directories. Since the Linux file system is hierarchical, we should immediately think of using a recursive approach: as a base case, we list all files in a directory with no sub-directories. Otherwise, we list all files and directories, and recursively call our function on every subdirectory. You can see this approach in action with the following command (enter into the terminal/shell).

```bash
ls -R testpages/
```

The command will list all files and directories recursively: you can see all the files and the level2 directory in `lab/testpages/`, and then all files in the directory `lab/testpages/level2`. As you can probably guess, the command option -R tells the listing to recursively go down the directory tree.

Then try the following commands with the program using Linux terminal/shell.
```bash
ls -R ../
ls -R ~
```

### Running `main.py`
You will be prompted to enter a starting directory.  Try filling in the prompt as follows.  (Note: if you created a differently-named directory for the `lab` files at the start of the lab, e.g. with a hyphen or without the 0, you will want to rename that directory as `lab`).
```
Enter a starting directory or file : `lab`
```
Then click return.  If everything works, you should see the full contents of the `lab` directory!

Observe the behavior of the program as it stands before you make any modifications. The given version of the program `dirs.py` lists the names of the files and sub-directories in a directory, but does not recursively list the files under any sub-directories.

#### Update to main.py file.
If you have already pulled here is an update to the `main.py` file that should help you run part 2 easier later on:


```python
# main.py
basedir = input('Enter a starting directory or file: ')

# PART 1 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
from lab.dirs import list_dir
list_dir( basedir )
# PART 1 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# PART 2 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# from lab.dirattrs import list_dir, FileStats
# fstats = FileStats()
# list_dir( basedir, fstats )
# fstats.print_results()
# PART 2 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
```


### Updating `dirs.py`
You are to modify the `dirs.py` program to _recursively_ print the names of all the files in all sub-directories. Here are some details:

#### 1. You must use a recursive solution
#### 2. File names should be printed one per line.
#### 3. Output
Just before any recursive calls, print out a message `-- Entering [dir-name]` where your program should fill in the directory name "dir-name". Just after any recursive calls, print out `-- Leaving [dir-name]` where your program should fill in the directory name. For example, output should look like:

```bash
--Entering testpages
grading.html
index.html
level2
readme.txt
test2.html
test.html
--Entering level2
page1.html
page2.html
--Leaving level2
--Leaving testpages
```

**Warning:** for this task of the lab, you will only need to write a small number of lines of code. Go slowly and carefully, following the guidance below.

1. Python provides a few useful methods and functions in the `os` module and the os.path module that you need to use (read the relevant Python online documents for details).  Some of these are already in the code, and your first step might be to run the code a bunch of times in the `lab` directory, adding some print statements that help you understand what’s going on.
    - The `os` module has a function called `listdir()` that returns a Python list of the contents of the directory. The list contains both files and sub-directories.  When you run the code (and enter the directory `lab`), you can see this function in action: it’s being used in line `35`, leading to a bunch of files being printed in line `39`.  Read this link if you’d like more information: http://www.tutorialspoint.com/python/os_listdir.htm

    - Add a line like `print(v)` under line `39`.  Do you understand what the difference between `f` and `v` is?

    - While a directory contains a list of files and potentially subdirectories, a file doesn't have any directories. Thus you can't use the function `listdir()` to generate a list if the parameter to the function is a file itself. To check if an object is a file or a directory, you can use the function `isfile()` and `isdir()` in the `os`.path module, respectively.  You can search for them online.  Try adding print statements like `print(os.path.isfile(v))` and `print(os.path.isdir(v))` to understand what’s going on.  What more on how they work? Search for them online! E.g. search for `os.path.isfile()`.

    #### ASIDE/TIP
    When checking if an object is a file or a directory, the isfile() and isdir() functions require the parameter to be a full, absolute path. A relative path is something similar to the following: `~csci204/2023-spring/`, or `~/message.txt` or `../readme.txt` while an absolute path is a complete path from the root directory, such as: `/home/accounts/student/s/sam023/hello.txt`

    The problem is that `listdir()` doesn't give you an absolute path (ugh!). It gives you the file name or directory name.
    The good news is that `os.path` has you covered:
    `os.path.abspath(curr_dir_name)` - will take the name of a directory as input and convert it to the absolute path;
    `os.path.join(absolute_path, file_or_dir_name)` - will intelligently combine an absolute path with your file or directory name.

    You can see that `os.path.join` is being used in line `38`!

2. As usual, think about how you can break this exercise up into small parts and test as you go.  At a birds-eye view, the provided code has a line that checks if a path is not a directory.  You can use this for your base case (but will want it to include a return statement, which need not return anything).
    - To familiarize yourself with the os methods, first, try to create a list of all files and all directories.  The starter coder already iterates through these (and above, you saw how to check if the things being iterated over are files or directories).  You might:

        - Create empty lists to store all files/directories before entering the for loop (the for loop was originally at line 35, but may be slightly offset now depending on what code you have added).
        - For each file/directory f that the for loop iterates through, check if it is a file or directory.  Then add it to the appropriate list
        - At the end of the for loop, print your file list and directory list.  Make sure that they check out.

3. Now for recursion.
    - Note your base case already checks if a giving path is a directory. So, rather than sorting our directory contents into two lists, we'll leverage the base case to print.
    - Try replacing the code that sorts your directory contents into lists of files and directories with recursive calls to list_dir.
4. Finally, worry about the entering and leaving print statements.
It is OK to modify the last few lines of your program (from the basedir input on) to look like the following, which will handle the outermost --entering and --leaving statements.

```python
basedir = input("Please enter the starting path name : ")
# Call list_dir which lists directories and files recursively
# The argument is the starting file(dir)
print ( "--Entering : ", os.path.basename(basedir))
list_dir( basedir )
print ( "--Leaving : ", os.path.basename(basedir))
```

To check your program's output, run the file and enter the starting directory:
```bash
lab/testpages
```

Your listing should contain the same folders and files listed (albeit in a different format, or a different order since Python doesn't list files in a fixed order.) Here is a sample output:

```bash
--Entering testpages
grading.html
index.html
level2
readme.txt
test2.html
test.html
--Entering level2
page1.html
page2.html
--Leaving level2
--Leaving testpages
```

Run your program using at least two more different directories each of which has files and a sub-directory (or sub-directories). You must test your program using testpages.
Make sure your program is well commented.

## Get File Statistics When Traversing Directories
If you list files on Linux using commands such as `ls -l` or `ls -lt`, you will find that other file statistics are printed, including dates when the files are created and the size of the files. Try these commands in your shell (from your work directory) .
```python
ls -l ~/
ls -lt testpages
```

For now, we will just concentrate on one of the pieces of information, the size of each file. This will be in one of the middle columns in the above listing. For example, if you check the `lab` directory, the file `grading.html` in the testpages directory has a size of 667 bytes, or 667 characters since this is a text file in which each character is a byte long.

### Your tasks
Create a new program/file based on the `dirs.py` program you just finished: name the new program/file as `dirattrs.py`, for directory attributes. The new program will keep track of the maximum- and minimum-sized files in the directories searched. Also change the import in your `main.py` to refer to this new file instead.

The basic logic of the program is to define a FileStats class, and then create a FileStats object.  This object will store the maximum and minimum size of a file it has encountered so far.  You will create a class method that will update this data (maximum and minimum) as you recurse through files (for instance, if the max size of a file you’ve seen so far is 100 bytes, and you encounter a file that is 110 bytes, you will update the FileStats object).

Read on for how to modify the `dirattrs.py` program.

### Develop a FileStats class
1. Since you are going to be creating a series of statistics, create a new FileStats Python class with the following data attributes: `max_size` and `min_size`, along with the filenames associated with those sizes, `max_file` and `min_file` for example.
2. First, define two methods within `FileStats`.
    The constructor where you define your data attributes, which should take in 4 optional arguments (for the corresponding attributes);

    Note, for default values (i.e. `firstmax` and `firstmin` in the above code). As a hint, Python provides a sys.maxsize as a reasonable maximum integer value that a file size could be. What attribute would be useful to initialize to that value?.

    Note that there is really no limit on the values of numbers in Python.
    The `print_results(self)` method which prints the statistics in the following format:

    ```bash
    maximum size among files : 667 (lab/a/b/file.txt)
    minimum size among files : 53 (lab/c/d/otherfile.dat)
    ```

    **Note:** There is no `__str__` method, just `print_results`.

    **Note:** After writing the above two methods, test them!  You can, e.g., set both attributes to be `42, "testfile.txt"` just to make sure that the broad print structure works.
3. Now add a third method, `update(self, filename)` to carry out the task of retrieving the file statistics and updating the values held in your FileStats object.  For example, if the biggest file so far has size 100, and `filename` has size 200, you’ll want to update  See step 3 below for how to retrieve values that you’ll need to update.

    -  To retrieve file statistics, Python's os module provides a function called `lstat()`. The function `os.lstat()` returns an object. Among other pieces of information, the returned object contains the size of the file. This data member is called `st_size`. You can use them to collect the required statistics. Read the relevant Python document to make sure you understand how to access these values.
    - You might, e.g., try a line like `size = os.lstat(filename).st_size` somewhere (and might even try to put this line in dirs.py and print size, just to see how it works!)
4. The number of bytes a file takes is an integer, so you can print the maximum size and minimum size directly when the directory traversal is completed.

### Other Modifications
After writing your `FileStats` class, complete the following tasks to make the program work.

1. Copy your `list_dir()` function into your dirattrs.py file
2. Modify the `list_dir()` method so that it takes a FileStats object as a parameter. We ask that the `list_dir()` method recursively call itself, passing your updated FileStats object each time.
3. Update the `FileStats` object as you recursively traverse the directory.

4. Initialize a `FileStats` object before calling the `list_dir()` method. I.e. the last few lines of your code may now look like the following:
```python
fstats = FileStats()
print ( "--Entering : ", os.path.basename( basedir ))
list_dir( basedir, fstats )
print ( "--Leaving : ", os.path.basename( basedir ))
fstats.print_results()
```

## The Final Product
Make sure your program works correctly in at least two directory listings, each of which must have multiple levels of directories. The first must be the directory
```
lab/testpages/
```

The test run should show the following values (with actual correct file paths):
```
maximum size of files : 667 (associated file path from basedir)
minimum size of files : 53 (associated file path from basedir)
```

## Submission
Review your programs and make sure your programs follow proper styles including naming and comments. Remove extra printing statements you may have put in place during the development of the program. Format the programs properly.

Make sure at the top of each program you include a global comment section following the sample below that indicates the lab assignment, your name, your lab section, and your professor's name. If you worked with a partner, include both names.
```python
'''CSCI 204 Lab Recursion
Lab section: CSCI 204.L61, Tuesday 10-11:52
Student name: Sam Snoopy
Instructor name: Professor Garfield'''
```

Finally, submit your lab!  As in previous labs, you should submit via gradescope. Double check you have both `dirs.py` and `dirattrs.py` (which should include your FileStats class). You do not need to upload any other files.
