n=int(input("\nEnter the number of rows:"))
for i in range(1,n+1):
    for j in range(0,i):
        print(i,end="  ")
    print("\r")
