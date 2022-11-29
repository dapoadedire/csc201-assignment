#  Hailstone algorithm


def hailstone(n):
    if n == 1:
        print(n)
    elif n % 2 == 0:
        print(n)
        hailstone(n / 2)
    else:
        print(n)
        hailstone(3 * n + 1)
