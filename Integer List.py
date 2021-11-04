listA = [10, 20, 30, 40, 50]
listB = []

for i in range(len(listA)):
    if i == 0:
        num = listA[i] + listA[i+1]
        listB.append(num)

    elif i == 4:
        num = listA[i] + listA[i-1]
        listB.append(num)
    
    else:
        num = listA[i] + listA[i-1] + listA[i+1]
        listB.append(num)

print("\nList A: ", listA)
print("\nList B: ", listB)