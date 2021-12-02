import math

x = float(input('x: '))

n = math.floor(x)

if n<0:
    y = 0
elif n%2 == 0:
    y = 1
elif n%2 == 1:
    y = -1
else:
    print ('dead')

print (y)
