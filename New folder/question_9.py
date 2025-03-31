def generate_fibonacci(n):
# 9.      Write a program to sum the first 50 fibonacci sequence.

    fibonacci_sequence = [0, 1]  # Start with the first two terms
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return fibonacci_sequence
    
    # Generate subsequent terms
    for _ in range(2, n):
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    return fibonacci_sequence

# Step 1: Generate the first 50 Fibonacci numbers
n = 50
fib_sequence = generate_fibonacci(n)

# Step 2: Calculate the sum
fib_sum = sum(fib_sequence)

# Step 3: Print the results
print(f"The first {n} Fibonacci numbers are: {fib_sequence}")
print(f"Sum of the first {n} Fibonacci numbers: {fib_sum}")