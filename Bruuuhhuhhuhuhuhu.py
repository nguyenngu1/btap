def printlist():
    for i in range(column):
        print(list_a[i],end="")
size = int(input("Size: "))
list_a = []
row = size*2 + 1 
column = (size - 1)*4 +1
for i in range(column):
    list_a.append("-")
list_b = []
for i in range(size, 0, -1):
    list_b.append(chr(97+i))
a = column//2 
for i in range(row//2):
    for j in range(column//2):
        if size-1 >= i-j >= 0:
            list_a[a-(2*j)] = list_b[i-j]
            list_a[a+(2*j)] = list_b[i-j]
        else:
            break
    printlist()
    print("\n")
    list_a = []
    for i in range(column):
        list_a.append("-")
for i in range(row//2-2,-1,-1):
    for j in range(column//2):
        if size-1 >= i-j >= 0:
            list_a[a+(2*j)] = list_b[i-j]
            list_a[a-(2*j)] = list_b[i-j]
        else:
            break
    printlist()
    print("\n")
    list_a = []
    for i in range(column):
        list_a.append("-")