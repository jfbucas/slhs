import math

def pythagoras(a, b):
    return math.sqrt(a**2 + b**2)

# Test
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
print(f"The hypotenuse is: {pythagoras(a, b)}")
