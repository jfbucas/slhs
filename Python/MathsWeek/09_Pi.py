import random
import math

def estimate_pi(num_points):
    inside_circle = 0
    for _ in range(num_points):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            inside_circle += 1
    return (inside_circle / num_points) * 4

# Test
points = int(input("Enter the number of points for simulation: "))
print(f"Estimated value of Pi: {estimate_pi(points)}")
