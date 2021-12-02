while True:
    a = int(input('a: '))
    b = int(input('b: '))
    c = int(input('c: '))
    x = [a, b, c]
    l = min(x, key=lambda i: int(i))
    k = max(x, key=lambda i: int(i))
    print('min:',l,'max:',k)
