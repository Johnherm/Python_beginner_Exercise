num = int(input("Enter a number: \n "))
fact = 1
j = 1
for i in range(1,num+1):
    j = i+1
    fact=fact*j
print(f"{num}! = ",fact)
print(fact)
fact2 = fact
list_fact2 = list(fact2)
print(list_fact2)
