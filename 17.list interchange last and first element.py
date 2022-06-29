def swaplist(list):
    get=list[-1],list[0]
    list[0],list[-1]=get
    return list
newlist=[1,2,3,4,5,6,7,8,9]
print(swaplist(newlist))
