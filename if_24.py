import math
x = float(input('x: '))

if x>0:
    y = 2*math.sin(x)
elif x<=0:
    y = 6-x
else:
    print ('none')

print (y)
