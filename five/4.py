# Function to convert any lowercase in a string to uppercase 

def to_upper(str):
    # length of the string
    length = len(str)
    # empty string to store the result
    result = ""
    # loop through the string
    for i in range(0, length):
        # check if the character is lowercase
        if str[i] >= 'a' and str[i] <= 'z':
            # convert lowercase to uppercase
            result = result + chr(ord(str[i]) - 32)
        else:
            # add the character to the result
            result = result + str[i]
    return result

print(to_upper("hel@#lo w-39402orld"))
