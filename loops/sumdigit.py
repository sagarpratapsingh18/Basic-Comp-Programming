a = int(input("Enter the Number"))
sum = 0
while a > 0:
    digit = a % 10
    sum += digit
    a //= 10
print("Sum of digits is:", sum)