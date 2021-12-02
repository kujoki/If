while True:
    a = float(input('a: '))
    b = float(input('b: '))
    c = float(input('c: '))

    if (a<b and a<c and b<c) or (a>b and b>c and a>c):
        a = a*2
        b = b*2
        c = c*2
    else:
        a = -a
        b = -b
        c = -c

    print (a, b, c)
