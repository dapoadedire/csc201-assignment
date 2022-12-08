# Notes on Golden Ratio


# The golden ratio, also known as the golden section or divine proportion, is a mathematical concept that describes the relationship between two quantities that have the same ratio as 
# the ratio of their sum to the larger of the two quantities. 
# This ratio is approximately equal to 1.6180339887, and is often represented by the Greek letter phi (φ).

# The golden ratio has been used in art, architecture, and design throughout history, and is believed by many to be aesthetically pleasing. 
# It is also found in nature, appearing in the proportions of certain plants, animals, and other objects.

# To determine whether any two numbers are in golden ratio, we can compare their ratio to the golden ratio. 
# If their ratio is equal to the golden ratio, the two numbers are said to be in golden ratio.

# Check if 2 numbers are in golden ratio
# define a function to check if two numbers are in the golden ratio
def is_golden_ratio(a, b):
    # calculate the golden ratio
    phi = 1.618

    # check if the ratio of the two numbers is close to the golden ratio
    return abs(phi - (a/b)) < 0.01

# test the function with some examples
print(is_golden_ratio(3, 5))  # True
print(is_golden_ratio(8, 13))  # True
print(is_golden_ratio(21, 34))  # True
print(is_golden_ratio(5, 8))  # False
print(is_golden_ratio(13, 21))  # False
