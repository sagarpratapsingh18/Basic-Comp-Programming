#given an array and commpute tha sum of all the elements in an array ??

arr= [1,2,3,4,5]
ans=0
for i in arr:
    ans+=i
print(ans)

#given an array find the maximum element in an array ??
arr= [1,2,3,4,5]
maxi= arr[0]
for i in arr:
    if i>maxi:
        maxi=i
print(maxi)

#given an array and a target number find number of occurences of target in an array ??
arr= [1,2,3,4,5,1,2,1,1]
target=1
count=0
for i in arr:
    if i==target:
        count+=1
print(count)