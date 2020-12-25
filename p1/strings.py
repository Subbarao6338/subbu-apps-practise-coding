# palindrome
s1=str(input("enter string:"))
s2=s1.casefold()
v=['a','e','i','o','u','A','E','I','O','U']
rs=reversed(s1)
if(list(s1)==list(rs)):
    print("palindrome")
else:
    print("not palindrome")

v1=[c for c in s1 if c in v]
print(v1.count())