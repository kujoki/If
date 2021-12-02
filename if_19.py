while True:
    a = int(input('a: '))
    b = int(input('b: '))
    c = int(input('c: '))
    d = int(input('d: '))

    if a==b and a==c:
        print (4)
    elif a==b and b==d:
        print(3)
    elif a==c and a==d:
        print(2)
    elif b==c and b==d:
        print(1)
    else:
        print ('dead')
