# generate_binary_and_convert.py
import random
# 8.      Write a program that generates random 4 digits number of 0s and 1s and convert the generated number to base 10.
# Step 1: Generate a random 4-digit binary number
binary_number = ''.join(random.choice('01') for _ in range(4))

# Step 2: Convert the binary number to base 10 (decimal)
decimal_number = int(binary_number, 2)

# Step 3: Print the results
print(f"Generated binary number: {binary_number}")
print(f"Equivalent in base 10: {decimal_number}")