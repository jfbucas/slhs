import numpy as np

def matrix_addition(matrix1, matrix2):
    return np.add(matrix1, matrix2)

def matrix_multiplication(matrix1, matrix2):
    return np.dot(matrix1, matrix2)

# Test
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])

print("Matrix 1:")
print(matrix1)
print("Matrix 2:")
print(matrix2)

# Addition
print("Matrix Addition Result:")
print(matrix_addition(matrix1, matrix2))

# Multiplication
print("Matrix Multiplication Result:")
print(matrix_multiplication(matrix1, matrix2))
