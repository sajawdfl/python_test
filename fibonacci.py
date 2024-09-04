def fibonacci(n):
    a , b = 0 , 1
    ls = []
    for i in range(n):
        a , b = a , a + b
        a , b = b , a
        ls.append(b)
    return ls