N = int(input("What term do you want the value of? "))

num1 = 0 
num2 = 1
count = 0

while count < N-1:
       Nth = num1 + num2
    
       num1 = num2
       num2 = Nth
       count = count + 1

print(num1)