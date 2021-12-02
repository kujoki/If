while True:
    x = int(input('x: '))

    if x == 0:
        print ('Нулевое число')
    elif x>0 and x%2 == 0:
        print ('Положительное четное')
    elif x<0 and x%2 == 1:
        print ('Отрицательное нечетное')
    elif x>0 and x%2 == 1:
        print ('Положительное нечетное')
    elif x<0 and x%2 == 0:
        print ('Отрицательное четное')
    else:
        print('Error')
        
