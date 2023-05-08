# Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function

# Solution:

maxNumber = int(input("Enter a number: "))

oddNumbers = []
for i in range(maxNumber+1):
    if i%2 != 0:
        oddNumbers.append(i)