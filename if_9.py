while True:
    a = int(input('a: '))
    b = int(input('b: '))
    c = 0

    if a > b:
        c = a
        a = b
        b = c
        print ('a = ',a,'b = ',b)
    elif a < b:
        print ('a = ',a,'b = ',b)
    else:
        print('Числа одинаковы')
