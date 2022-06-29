a=0
b=1
c=0
n=int(input("Enter the limit:"))
print("\nThe Fibonacci Series is")
print(a)
print(b)
for i in range(0,n-2):
    c=a+b
    a=b
    b=c
    print(c)
