with open("input.txt", "r") as input_file:

    with open("output.txt", "w") as output_file:

        for line in input_file:

            value = round(float(line))

            output_file.write(str(value))
            output_file.write("\n")
