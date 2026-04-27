def calc_fibo(num: int) -> int:
    if num == 1 or num == 0:
        return num
    return calc_fibo(num - 1) + calc_fibo(num - 2)


num_of_elm = int(input("Enter the total number of elements:\n>> "))
print(f"The {num_of_elm} elements of the Fibonacci Series:\n")

for i in range(0, num_of_elm):
    print(calc_fibo(i))
