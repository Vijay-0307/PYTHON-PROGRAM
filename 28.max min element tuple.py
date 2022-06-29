str=(1,2,3,4,5)
j=0
for i in str:
    if i>j:
        j=i
k=str[0]
for k in str:
    if k<i:
        i=k

print("maximum=",j)
print("minimum=",i)