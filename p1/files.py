#n numbers
c=0
while(c<=9):
    print(c,end=" ")
    c=c+1
#even or odd
num=int(input("number:"))
for n in num:
    if n%2==0:
        print("even")
        break
    else:
        print("odd")
