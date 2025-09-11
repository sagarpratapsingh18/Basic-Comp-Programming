list= [1,2,3,4,5,6]
n= len(list)
for i in range(0,n//2):
    list[i],list[n-i-1]= list[n-i-1],list[i]
print(list)