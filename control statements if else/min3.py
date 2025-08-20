A = int(input("Enter A: "))
B = int(input("Enter B: "))
C = int(input("Enter C: "))

if A <= B and A <= C:
    print("Minimum =", A)
elif B <= A and B <= C:
    print("Minimum =", B)
else:
    print("Minimum =", C)
