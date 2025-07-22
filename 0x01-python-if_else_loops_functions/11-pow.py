def pow(a, b):
    result = 1
    if b < 0:
        # For negative powers, compute positive power and invert
        b = -b
        for _ in range(b):
            result *= a
        return 1 / result
    else:
        for _ in range(b):
            result *= a
        return result

