while True:
    a = int(input('a: '))
    b = int(input('b: '))
    c = int(input('c: '))
    #x = [a, b, c]
    #l = min(x, key=lambda i: int(i))
    #print(l)

    if a<b and b<c:
        mean = b
    elif c<b and b<a:
        mean = b
    elif b<a and a<c:
        mean = a
    elif c<a and a<b:
        mean = a
    elif a<c and c<b:
        mean = c
    elif b<c and c<a:
        mean = c
    else:
        print ('dead')

    #if a<b<c or c<b<a:
    #    print(b)
    #elif a<c<b or b<c<a:
    #    print(c)
    #elif b<a<c or c<a<b:
    #    print(a)
    #else:
    #    print('dead')

    print (mean)
