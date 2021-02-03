import numpy as np
a=np.array([1,2,3,4,5])
print("a",a)
# copy and view
c=a.copy()
v=a.view()
a[0]=10
print("a",a)
print("c",c)
print("v",v)
v[0]=7
print("a",a)
print("c",c)
print("v",v)
print("c",c.base)
print("v",v.base)

# shape
a=np.array([[1,2,3,4],[5,6,7,8]])
print(a,a.shape)

b=a.reshape(4,2)
print(b)

a=np.array([1,2,3,4,5],ndmin=5)
print(a,a.shape)
for i,j in np.ndenumerate(a):
    print(i,j)
b=a.reshape(-1)
print(b)

# iter
'''l=[]
s=int(input("size:"))
print("array elements:")
for n in range(s):
    ele=int(input())
    l.append(ele)
print(l)
x=np.array(l)
print(x)
for i in np.nditer(x):
    print(i,end=" ")
for i in np.nditer(x[::2]):
    print(i,end=" ")
for i,j in np.ndenumerate(x):
    print(i,j)
'''
# concatenate
a1=np.array([[1,2,3],[7,8,9]])
a2=np.array([[4,5,6],[10,11,12]])
y=np.concatenate((a1,a2))
print(y)
y=np.concatenate((a1,a2),axis=1)
print(y)
h=np.hstack((a1,a2))
print(h)
v=np.vstack((a1,a2))
print(v)
d=np.dstack((a1,a2))
print(d)
n=np.array_split(y,3,axis=1)
print(n)

# search
a=np.array([1,2,3,4,5,6,7])
x1=np.where(a==4)
print(x1)
x2=np.where(a%2==0)
print(x2)
x3=np.where(a%2==1)
print(x3)
x4=np.searchsorted(a,5)
print(x4)
x5=np.searchsorted(a,[2,4,5])
print(x5)