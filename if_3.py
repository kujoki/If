while True:
    a = int(input('Ввести a: '))

    if a>0:
       a = a+1
    elif a<0:
       a = a-2
    elif a==0:
        a = 10
    else:
        print('Ошибка в рассуждениях')
    print(a)
