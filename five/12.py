def max6(integers):
    integers_list = integers.split(" ")
    max_integers = max(integers_list)

    return max_integers

def main():
    integers = input("Enter integers: ")
    max_integers = max6(integers)
    print("Max integer is", max_integers)

main()