# Notes on Golden Ratio


# The golden ratio, also known as the golden section or divine proportion, is a mathematical concept that describes the relationship between two quantities that have the same ratio as the ratio of their sum to the larger of the two quantities. This ratio is approximately equal to 1.6180339887, and is often represented by the Greek letter phi (φ).

# The golden ratio has been used in art, architecture, and design throughout history, and is believed by many to be aesthetically pleasing. It is also found in nature, appearing in the proportions of certain plants, animals, and other objects.

# To determine whether any two numbers are in golden ratio, we can compare their ratio to the golden ratio. If their ratio is equal to the golden ratio, the two numbers are said to be in golden ratio.

# Check if 2 numbers are in golden ratio

def golden_ratio(a, b):
  # Define the golden ratio
  GOLDEN_RATIO = (1 + 5**0.5) / 2

  # Compute the ratio of the two numbers
  ratio = a / b

  # Check if the ratio is equal to the golden ratio within a given tolerance
  if abs(ratio - GOLDEN_RATIO) < 1e-6:
    return True
  else:
    return False
