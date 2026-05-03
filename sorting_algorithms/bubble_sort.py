arr = [int(val) for val in input("Enter the array:\n>> ").split()]
n = len(arr)
for i in range(n-1):
    for j in range(n-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

print("Sorted Array: ", arr)