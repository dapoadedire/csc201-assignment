def checkTriangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False

print(checkTriangle(3, 4, 9))