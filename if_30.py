while True:
    x = int(input('x: '))

    if x == 0:
        print ('Нулевое число')
    elif x//100>0 and x%2 == 1:
        print ('Трехзначное нечетное')
    elif x//100>0 and x%2 == 0:
        print ('Трехзначное четное')
    elif x//100 == 0 and x%2 == 1 and x//10 != 0:
        print ('Двухзначное нечетное')
    elif x//100 == 0 and x%2 == 0 and x//10 != 0:
        print ('Двухзначное четное')
    elif x%2 == 1 and x//10 == 0:
        print ('Однозначное нечетное')
    elif x%2 == 0 and x//10 == 0:
        print ('Однозначное четное')
    else:
        print ('none')
