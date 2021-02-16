import scipy as sp
from scipy import cluster
from scipy import integrate
#print(sp.info())
#print(sp.source(cluster))
#print(help(cluster))
a=sp.special.exp10(3)
print(a)
b=sp.special.exp2(3)
print(b)
c=sp.special.sindg(90)
print(c)
d=sp.special.cosdg(0)
print(d)
i=integrate.quad(lambda x:sp.special.exp10(x),0,1)
print(i)
e=lambda x,y:x*y**2
f=lambda x:1
g=lambda x:-1
h=integrate.dblquad(e,0,2,f,g)
print(h)