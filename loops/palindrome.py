A = int(input("Enter A: "))
num = A
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10

if rev == A:
    print("Yes")
else:
    print("No")
