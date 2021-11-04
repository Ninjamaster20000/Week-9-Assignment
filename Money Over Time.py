print("Starting at 1 penny on day 1, each day the salary is doubled")
days = int(input("Enter the number of days to calculate: "))
print()

count = 1
total = 0

for i in range(days):

    money = count / 100

    print("Day ", i+1, ": $", money, sep='')

    count = count * 2
    total = total + money

print("Total: $", total)