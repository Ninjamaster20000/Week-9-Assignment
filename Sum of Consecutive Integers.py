num = int(input("Enter an integer to add its consecutive integers: "))
print()
total = 0

for i in range(num):
    total = total + (i + 1)
    print(total)

print("\nSum of consecutive integers up to ", num, ": ", total, sep = "")