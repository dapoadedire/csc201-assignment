# Discuss in details the process of file operation in Python. In addition, explain with practical illustrations, the need for close() statement in Python.


# In Python, the open() function is used to open a file for reading or writing. It takes in the file path as an argument and returns a file object which can be used to read or write to the file.

# Here is an example of how to open a file for reading:

file = open("file.txt", "r")
contents = file.read()
print(contents)

file.close()


# And here is an example of how to open a file for writing:

file = open("file.txt", "w")
file.write("Hello, world!")

file.close()


# It is important to close the file after you are done reading or writing to it. This is because when you open a file, your system allocates some resources to manage the file. 
# If you forget to close the file, these resources will remain allocated even after you are done with the file. This can lead to resource exhaustion and affect the performance of your system.

# The close() method is used to close a file. It is generally a good practice to use the with statement when working with files, 
# as it automatically closes the file after the indented code block is executed. Here is an example:


with open("file.txt", "r") as file:
    # Read the contents of the file
    contents = file.read()

    # Print the contents of the file
    print(contents)

# The file is automatically closed here
# In summary, the process of file operations in Python involves:

# Opening the file using the open() function.
# Reading from or writing to the file using the file object's methods.
# Closing the file using the close() method or the with statement.
# It is important to close the file to free up the resources allocated to it and to avoid potential performance issues.
