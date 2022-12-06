# Open file1.txt in read mode
with open("file1.txt", "r") as file1:
  # Open file2.txt in write mode
  with open("file2.txt", "w") as file2:
    # Read each line from file1.txt
    for line in file1:
      # Write the line to file2.txt
      file2.write(line)
