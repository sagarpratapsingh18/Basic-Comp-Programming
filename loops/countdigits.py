#sum of the digits
a = int(input("Enter a number: "))
count = 0
while a > 0:
    a //= 10
    count += 1
print("The number of digits is", count)

