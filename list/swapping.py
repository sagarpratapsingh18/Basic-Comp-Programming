#swapping elements using for loop and swap function
l = [1,2,3,4,5]
def swap(a,b):
    temp = a
    a = b
    b = temp
    return a,b
for i in range(0,len(l)-1,2):
    l[i],l[i+1] = swap(l[i],l[i+1])
print(l)
