# Take command line arguments and print them out as a list.


comma_separated = input("Input values: ")

values_list = comma_separated.split(",")


# As tuple

values_tuple = tuple(values_list)
