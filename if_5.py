while True:
    a = int(input('a: '))
    b = int(input('b: '))
    c = int(input('c: '))

    k = 0
    n = 0

    if a>0:
        k = k+1
    elif a == 0:
        k = k
    else:
        n = n+1
        
    if b>0:
        k = k+1
    elif b == 0:
        k = k
    else:
        n = n+1
    
    if c>0:
        k = k+1
    elif c == 0:
        k = k
    else:
        n = n+1

    print ('Количество положительных чисел:', k)
    print ('Количество отрицательных чисел:', n)

