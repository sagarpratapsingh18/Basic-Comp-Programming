# givrn list is an integers and a target number find and print index of a target number in the given list.

arr = list(map(int, input("Enter the array: ").split()))
target = int(input("Enter the target: "))

for i in range(len(arr)):
    print("index of", arr[i], "is", i)
    if arr[i] == target:
        print("index of target is:", i)

if target not in arr:
    print("target not found")
