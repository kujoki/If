while True:
    a = int(input('a: '))
    b = int(input('b: '))
    c = int(input('c: '))

    if a<=c and a<=b:
        min = a
    elif c<=a and c<=b:
        min = c
    elif b<=a and b<=c:
        min = b
    else:
        print ('dead')

    print(min)
