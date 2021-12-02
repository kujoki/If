while True:
    a = int(input('a: '))
    b = int(input('b: '))

    if a != b:
        c = a+b
        a = c
        b = c
        # a, b = a+b, a+b
        print ('a = ',a,'b = ',b)
    else:
        a = 0
        b = 0
        print ('a = ',a,'b = ',b)

