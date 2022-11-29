#  Sort input values

values = input("Input values: ")

# turn values to list

values_list = values.split()

# Sort values

values_list.sort()

# Turn values to string

values = " ".join(values_list)

# Print values

print(values)
