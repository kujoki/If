while True:
    print ('Первая координата:')
    x_1 = int(input('x: '))
    y_1 = int(input('y: '))
    print ('Вторая координата:')
    x_2 = int(input('x: '))
    y_2 = int(input('y: '))
    print ('Третья координата:')
    x_3 = int(input('x: '))
    y_3 = int(input('y: '))

    if x_1 == x_2:
        x_4 = x_3
    elif x_1 == x_3:
        x_4 = x_2
    elif x_2 == x_3:
        x_4 = x_1
    else:
        print ('dead')

    if y_1 == y_2:
        y_4 = y_3
    elif y_1 == y_3:
        y_4 = y_2
    elif y_2 == y_3:
        y_4 = y_1
    else:
        print ('dead')

    print ('Координаты точки:','(',x_4,',',y_4,')')
