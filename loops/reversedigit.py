#reverse of a digit
a = int(input("Enter the Number: "))
reverse = 0
while a > 0:
    digit = a % 10
    reverse = reverse * 10 + digit
    a //= 10
print("Reverse of the number is:", reverse)
