# The Fibonacci sequence is a sequence in which each number is the sum of the two preceding ones.

def fibonacci(n):
    sequence = [0, 1]
    for i in range(2, n):
        next_term = sequence[i - 1] + sequence[i - 2]
        sequence.append(next_term)
    return sequence

# Test
terms = int(input("Enter the number of terms: "))
print(f"Fibonacci sequence: {fibonacci(terms)}")

