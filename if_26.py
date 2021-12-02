while True:
    x = int(input('Enter x: '))

    if x<=0:
        y = -x
    elif x >=2:
        y = 4
    elif x>0 and x<2:
    # elif 0<x<2:
        y = x**2
    else:
        print ('mistake')

    print (y)
    
