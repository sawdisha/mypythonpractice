# Question: print the elementt of list if it is greater or equal to the next element of list

# take the input list from user
arr = input("Provide the list of numbers seprated by space:").split()

# covert the elements of list from str to int
for i in range(len(arr)):
    arr[i] = int(arr[i])
print(len(arr))
# logic to verify if element of list is greater or equal to the next item from the list
for i in range(len(arr) - 1):
    if arr[i] >= arr[i+1]:
        print(arr[i])

print(arr[len(arr)-1])
