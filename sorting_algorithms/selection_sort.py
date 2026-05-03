arr = [int(val) for val in input("Enter the array:\n>> ").split()]
n = len(arr)
for i in range(n-1):
    minimum = i
    for j in range(i+1, n):
        if arr[j] < arr[minimum]:
            minimum = j
    arr[i], arr[minimum] = arr[minimum], arr[i]

print("Sorted Array: ", arr)