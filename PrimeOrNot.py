your_number = input("Enter the Number: ")
your_number = int(your_number)
count = 0
for i in range (1, your_number+1):
    if your_number%i==0:
        count = count+1
if count == 2:
    print("Prime")
else:
    print("Not Prime")
    