list1 = []
n = int(input("Enter number of elements in list: "))
for i in range(1, n + 1):
    element = int(input("Enter elements: "))
    list1.append(element)
print("Smallest element is:", min(list1))
print(list1)