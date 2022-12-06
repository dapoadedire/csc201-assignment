# Open the input file in read mode
with open("input.txt", "r") as input_file:
  # Open the output file in write mode
  with open("output.txt", "w") as output_file:
    # Read each line from the input file
    for line in input_file:
      # Convert the line to a float and round it to the nearest integer
      value = round(float(line))
      # Write the integer value to the output file
      output_file.write(str(value))
      output_file.write("\n")


# with open("./seven/new.txt", "w") as f:
#     f.write("Hello world")