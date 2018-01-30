import pylab

xVals = [2, 3, 4, 5]
yVals1 = [2, 3, 4, 5]
pylab.plot(xVals, yVals1, 'b-', label = 'Test1')
yVals2 = [1, 7, 3, 5]
pylab.plot(xVals, yVals2, 'r--', label = 'Test2')
pylab.legend()

pylab.show()