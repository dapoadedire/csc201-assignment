# Take input from user and calculate average and sum untin user enters 0.


# Compare this snippet from three/13.py:

sum = 0
average = 0
count = 0

num = int(input("Enter a number greater than 0 (less than 0 to quit): "))

while num != 0:
    sum += num
    count += 1
    num = int(input("Enter a number greater than 0 (less than 0 to quit): "))

average = sum / count

print(f"Average: {average}")
print(f"Sum: {sum}")
