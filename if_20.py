while True:
    a = int(input('a: '))
    b = int(input('b: '))
    c = int(input('c: '))

    ab = abs(a-b)
    ac = abs(a-c)

    if ab>ac:
        print ('Точка C расположена ближе, расстояние до точки А:',ac)
    elif ab<ac:
        print ('Точка B расположена ближе, расстояние до точки А:',ab)
    elif ab==ac:
        print ('Расстояние одинаково и равно:',ac)
    else:
        print('dead')
