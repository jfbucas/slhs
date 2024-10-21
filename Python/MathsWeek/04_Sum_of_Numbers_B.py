def sum_of_natural_numbers(n):
    return n * (n + 1) // 2

# Test
num = int(input("Enter a number: "))
print(f"The sum of the first {num} natural numbers is {sum_of_natural_numbers(num)}")
