# vowels count
s=str(input("string:"))
'''v=set("aeiouAEIOU")
c=0
for i in s:
    if i in v:
        c+=1
print("no. of vowels:",c)

# substring in a string
sub=input("substring:")
if sub in s:
    print("yes")
else:
    print("no")

# anagram strings
s2=input("str2:")
if(sorted(s)==sorted(s2)):
    print("anagrams")
else:
    print("not anagrams")

# print name format
l=s.split()
n=""
for i in range(len(l)-1):
    s=l[i]
    n+=s[0].upper()+"."
n+=l[-1].title()
print(n)

# frequent words in string
from collections import Counter
c=Counter(l)
n=int(input("no of frequent words"))
f=c.most_common(n)
print(f)

# string concatenation
se1=set(s)
se2=set(s2)
c1=list(se1 and se2)
uc=[c for c in s if c not in c1]+[c for c in s2 if c not in c1]
print("uncommon","".join(uc))
print("common","".join(c1))
un=se1.union(se2)
in1=se1.intersection(se2)
print("".join(un))
print("".join(in1))

# remove duplicate words
d="".join(se1)
print(d)

# sort
ss=input("string:")
w=ss.split(" ")
nw=" ".join(sorted(w))
nr=" ".join([word[::-1] for word in w])
ns=" ".join(reversed(w))
print(nw)
print(nr)
print(ns)

# count each word
from collections import Counter
w=str(input("word"))
a=s.split(" ")
c=0
for i in range(len(a)):
    if(w==a[i]):
        c+=1
print(w,c)

# list to string
l=[]
le=int(input("size"))
print("elements")
for i in range(le):
    e=input("")
    l.append(e)
s="".join(l)
print(s)

# remove ith char
i=int(input("ith"))
a=s[:i]+s[i+1:]
print(a)
'''
# remove duplicates
r=s.split(" ")
for i in range(len(r)):
    for j in range(i+1,len(r)):
        if (r[i]==r[j] and i!=j):
            r[j]="t"
for k in range(len(r)):
    if(r[k]!="t"):
        print(r[k],end=" ")
'''
#2
s1=set(r)
s2="".join(s1)
print(s1,s2)

# count of word
s1=list(s)
for i in range(len(s1)):
    print(s1[i],"-",s.count(s1[i]))
'''