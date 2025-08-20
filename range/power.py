a=int(input("Enter the base: "))
b=int(input("Enter the exponent: "))
result = 1
for i in range(b):
    result *= a
print(result, end=' ')