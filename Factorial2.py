num = int(input("Enter a number: \n "))
fact = 1
j = 1
for i in range(1,number+1):
    j = i+1
    fact=fact*j
print(f"{num}! = ",fact)
