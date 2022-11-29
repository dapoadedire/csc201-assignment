myList = [1, 4, 7, 0, 2, (3, 4, 5), 6, 9, 8]

count = 0

for i in myList:
    if type(i) == tuple:
        print("Tuple found at index", count)
        break
    count += 1

print(count)
