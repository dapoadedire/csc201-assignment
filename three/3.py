def y(t):
    if t < 0:
        return -3 * t**2 + 3 * t + 5
    elif t == 0:
        return 3 * t**2 - 3 * t + 5
    elif t > 0:
        return 3 * t**2 - 3 * t - 5


print(y(8))
print(y(-2))
print(y(0))
