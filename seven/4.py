# Open the input file in read mode
with open("input.txt", "r") as input_file:
  # Initialize the largest and smallest values
  largest = float("-inf")
  smallest = float("inf")
  # Read each line from the input file
  for line in input_file:
    # Convert the line to an integer
    value = int(line)
    # Update the largest and smallest values if necessary
    largest = max(largest, value)
    smallest = min(smallest, value)
  # Print the largest and smallest values
  print(f"Largest: {largest}")
  print(f"Smallest: {smallest}")
