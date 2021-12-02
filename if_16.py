while True:
    a = float(input('a: '))
    b = float(input('b: '))
    c = float(input('c: '))

    if a<b<c:
        a = a*2
        b = b*2
        c = c*2
    else:
        a = -a
        b = -b
        c = -c

    print (a, b, c)
