def swapPositions(list,pos1,pos2):
    list[pos1],list[pos2]=list[pos2],list[pos1]
    return list

list=[4,5,85,47,2584,236541]
pos1=int(input("Enter Position 1 want to interchange:" ))
pos2=int(input("Enter Position 2 want to interchange:" ))
print(list)
print(swapPositions(list,pos1-1,pos2-1))



