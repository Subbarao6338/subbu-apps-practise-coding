'''
# interst
p=float(input("Principle:"))
t=float(input("time(months):"))
r=float(input("interst:"))
si=(p*t*r)/100
ci=p*(pow((1+r/100),t))-p
print("si:",si,round(si))
print("ci:",round(ci))

# sum of numbers
n=int(input("n:"))
s1=[x for x in range(n+1)]
s2=[x*x for x in range(n+1)]
s3=[x**3 for x in range(n+1)]
print(s1)
print(s2)
print(s3)
print(sum(s1),sum(s2),sum(s3))

# area of circle
import math
r=float(input("radius:"))
A=math.pi*r*r
C=2*math.pi*r
print("area ",A)
print("circumference ",C)

# area of rectangle
length=float(input("length:"))
breadth=float(input("breadth:"))
AR=length*breadth
print(AR)
height=float(input("height:"))
v=length*breadth*height
print(v)

# display power of n
n=int(input("enter number:"))
t=int(input("no of terms:"))
#r=list(map(lambda x:n**x,range(t)))
r=[n**x for x in range(t)]
print("total terms are:",t)
print(r)

# factors of number
n=int(input("enter number:"))
f=[i for i in range(1,n+1) if (n%i==0)]
print(f)

#prime number
n=int(input("n:"))
l=[]
for i in range(2,n):
    c=0
    for j in range(2,i):
        if(i%j==0):
            c+=1
    if(c==0):
        l.append(i)
print(l)
for i in range(0,len(l),2):
    print(l[i],end=" ")

#decimal to binary
n=int(input("n:"))
l=[]
while(n!=0):
    d=n%2
    l.append(d)
    n=int(n/2)
print(l)
print(l[::-1])
l1=l[::-1]
for i in range(len(l1)):
    print(l1[i],end="")

#decimal to hexa
n=int(input("n:"))
l=[]
while(n!=0):
    d=n%16
    l.append(d)
    n=int(n/16)
print(l)
print(l[::-1])
l1=l[::-1]
for i in range(len(l1)):
    print(l1[i],end=" ")

# binary to decimal
n=int(input("n:"))
s=0
c=0
while(n!=0):
    d=n%10
    s=s+d*(2**c)
    n=int(n/10)
    c+=1
print(s)

# decimal to binary
n=int(input("decimal no:"))
t=n
b=""
while t>0:
    d=t%2
    b=str(d)+b
    t//=2
print(b)
'''
