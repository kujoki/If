while True:
    x = int(input('Enter x:'))
    y = int(input('Enter y:'))

    if x==0 and y==0:
        print ('0')
    elif x!=0 and y==0:
        print ('1')
    elif x==0 and y!=0:
        print ('2')
    elif x!=0 and y!=0:
        print('3')
    else:
        print ('dead')
