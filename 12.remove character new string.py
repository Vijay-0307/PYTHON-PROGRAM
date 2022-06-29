s=input("Enter a string:")
import re
s1=re.sub("[^0-9!@#$%^&*()_+]","",s)
print (s1)
r=input("Enter a string:")
r1=re.sub("[^a-z]","",r)
print(r1)