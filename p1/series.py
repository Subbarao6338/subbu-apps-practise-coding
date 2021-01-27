# fibonacci
#n th term
n=int(input("n:"))
def fibonacci(n):
    a = 0
    b = 1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1:
        return b
    else:
        for i in range(1, n):
            c = a + b
            a = b
            b = c
        return b
print(fibonacci(n))
#series
a=0
b=1
if n<=0:
    print(a)
else:
    print(a,b,end=" ")
    for i in range(0,n):
        c=a+b
        print(c,end=" ")
        a=b
        b=c
#check
import math
def perfectsquare(x):
    s=int(math.sqrt(x))
    if (s*s==x):
        return x
def fib(i):
    s1=perfectsquare(5*i*i+4)
    s2=perfectsquare(5*i*i-4)
    if (s1 or s2):
        print(i,"is fib num")
    else:
        print(i,"is not fib num")
n=int(input("enter number:"))
print(fib(n))
#range
l=int(input("lower range:"))
u=int(input("upper range:"))
for f in range(l,u+1):
    print(fib(f))

# armstrong number
#range
l = int(input("lower range"))
u = int(input("upper range"))
for n in range(l, u + 1):
    s=0
    c=0
    t=n
    while t>0:
        c=c+1
        t=t//10
    s=0
    t=n
    while t>0:
        d=t%10
        s=s+(d**c)
        t//=10
    if n==s:
        print(n,end=" ")
'''
