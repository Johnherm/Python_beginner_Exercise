number = int(input("Enter a number: \n"))
fact = 1
i = 1
while i <= number:
    fact = fact*i
    i = i +1
print(f"{number}! = ",fact)