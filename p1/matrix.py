import numpy as np
m = np.array([[12, 23, 34], [45, 56, 67], [78, 89, 90]])

# determinant
det1 = np.linalg.det(m)
print(det1)

# flatten
f=m.flatten()
print(f)

# diagonal
dai=m.diagonal()
print(dai)

# trace
tr=m.diagonal().sum()
print(tr)

# inverse if det!=0
i=np.linalg.inv(m)
print(i)

# transpose
mt=m.T
print(mt)

# identity
idt=np.identity(3)
print(idt)

# ones
o=np.ones(3)
print(o)

# zeros
z=np.zeros(3)
print(z)

# eye
e=np.eye(3,2)
print(e)

# ravel
r=np.ravel(m)
print(r)