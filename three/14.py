sum = 0
product = 1
count = 0

num = int(input("Enter a number greater than 0 (less than 0 to quit): "))
while num > 0:
    sum += num

    product *= num

    count += 1

    num = int(input("Enter a number greater than 0 (less than 0 to quit): "))

arithmetic_mean = sum / count

geometric_mean = product ** (1 / count)

print(f"Arithmetic Mean: {arithmetic_mean}")
print(f"Geometric Mean: {geometric_mean}")
