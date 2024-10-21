def sum_of_natural_numbers_stupid(n):
    total = 0
    for i in range(n+1):
        total = total + i
    return total

# Test
num = int(input("Enter a number: "))
print(f"The sum of the first {num} natural numbers is {sum_of_natural_numbers_stupid(num)}")
