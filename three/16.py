# Notes on Golden Ratio


# Check if 2 numbers are in golden ratio

def golden_ratio(a, b):
    if a / b == (1 + 5 ** 0.5) / 2:
        return True
    else:
        return False