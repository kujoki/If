while True:
    x = int(input('Enter: '))

    if (x%4 == 0 and x%100 != 0) or x%400 == 0:
        y = 366
    else:
        y = 365

    print (y)
