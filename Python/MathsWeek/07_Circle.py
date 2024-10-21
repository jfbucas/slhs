import math

def circle_area_and_circumference(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference

# Test
r = float(input("Enter the radius of the circle: "))
area, circumference = circle_area_and_circumference(r)
print(f"Area: {area}")
print(f"Circumference: {circumference}")
