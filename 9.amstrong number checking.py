sum=0
r=0
n=int(input("Enter a number:"))
temp=n
while (n>0):
    r=n%10
    sum=sum+(r*r*r)
    n=n//10
if temp==sum:
    print("The Given number is amstrong number")
else:
    print("The Given number is not a amstrong number")
