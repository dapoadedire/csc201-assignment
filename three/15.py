#  Calculate harmonic mean of many numbers

sum = 0
count = 0

num = int(input("Enter a number greater than 0 (less than 0 to quit): "))

while num > 0:
    sum += 1 / num
    count += 1
    num = int(input("Enter a number greater than 0 (less than 0 to quit): "))

harmonic_mean = count / sum

print(f"Harmonic Mean: {harmonic_mean}")