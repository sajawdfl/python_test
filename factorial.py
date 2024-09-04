def factorial(num):
    f = 1
    for i in range(num):
        f = num * f
        num -= 1
    return f