A = [1, 2, 3, 4]
even = 0
odd = 0
for x in A:
    if x % 2 == 0:
        even += 1
    else:
        odd += 1
print(abs(even - odd))
