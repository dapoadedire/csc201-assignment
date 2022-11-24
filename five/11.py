def swap(a, b):
    a, b = b, a
    return a, b

def main():
    a = input("Enter A: ")
    b = input("Enter B: ")
    a, b = swap(a, b)   
    print("A =", a)
    print("B =", b)

main()  
