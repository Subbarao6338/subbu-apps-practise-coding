'''#n numbers
c=0
while(c<=9):
    print(c,end=" ")
    c=c+1
#even or odd
n=int(input("number:"))
for i in range(n):
    if i%2==0:
        print("even")
        break
    else:
        print("odd")


# armstrong
n=int(input("number:"))
c=0
t=n
while t>0:
    t=t//10
    c+=1
s=0
t=n
while t>0:
    d=t%10
    s=s+(d**c)
    t=t//10
if n==s:
    print("armstrong")
else:
    print("not armstrong")

# armstrong series
n= int(input("num"))
for i in range(n):
    c=0
    t=i
    while t>0:
        c=c+1
        t=t//10
    s=0
    t=i
    while t>0:
        d=t%10
        s=s+(d**c)
        t=t//10
    if i==s:
        print(i,end=" ")
'''
#hexa to octa
n=int(input("n:"))
h=0
c=0
while(n!=0):
    d=n%10
    h=h+d*(16**c)
    n=int(n/10)
    c+=1
print(h)
t=h
o=""
while t>0:
    d=t%8
    o=str(d)+o
    t//=8
print(o)
