# add elemnts to array
l=[]
s=int(input("size:"))
print("array elements:")
for n in range(s):
    ele=int(input())
    l.append(ele)
print(l)

print(min(l))
print(max(l))
print(sum(l))
print(max(l)-min(l))
a=sum(l)/s
print(a)
l.sort()
print(l)

# left rotation
def lR(arr,d,n):
    for i in range(d):
        temp=arr[0]
        for j in range(n-1):
            arr[j]=arr[j+1]
        arr[n-1]=temp
r=int(input("no of rotated terms:"))
lR(l,r,s)
print(l)