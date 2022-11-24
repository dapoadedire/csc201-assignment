def min6(integers):
    integers_list = integers.split(" ")
    min_integers = min(integers_list)

    return min_integers

def main():
    integers = input("Enter integers: ")
    min_integers = min6(integers)
    print("min integer is", min_integers)

main()