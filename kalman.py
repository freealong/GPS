import numpy
import pylab

n_iter = 50
sz = (n_iter,)
x = -0.37727
z = numpy.random.normal(x,0.1,size=sz)
Q = 1e-5

xhat = numpy.zeros(sz)
P = numpy.zeros(sz)
xhatminus = numpy.zeros(sz)
Pminus = numpy.zeros(sz)
K = numpy.zeros(sz)
R = 0.1**2

xhat[0] = 0.0
P[0] = 1.0
for k in range(1,n_iter):
    xhatminus[k] = xhat[k-1]
    Pminus[k] = P[k-1] + Q
    K[k] = Pminus[k]/(Pminus[k] + R)
    xhat[k] = xhatminus[k]+K[k]*(z[k]-xhatminus[k])
    P[k] = (1-K[k])*Pminus[k]
pylab.figure()
pylab.plot(z,'k+',label='noisy measurements')
pylab.plot(xhat,'b-',label='a posteri estimate')
pylab.axhline(x,color='g',label='truth value')
pylab.legend()
pylab.xlabel('Iteration')
pylab.ylabel('Voltage')
pylab.figure()
valid_iter = range(1,n_iter) # Pminus not valid at step 0
pylab.plot(valid_iter,Pminus[valid_iter],label='a priori error estimate')
pylab.xlabel('Iteration')
pylab.ylabel('$(Voltage)^2$')
pylab.setp(pylab.gca(),'ylim',[0,.01])
pylab.show()
