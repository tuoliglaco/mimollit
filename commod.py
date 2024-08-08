import random

def generate_balance_frequency():
    # Generate a random frequency between a specified range
    return random.uniform(0.5, 2.0)  # Example range: 0.5 to 2.0

# Example usage:
balance_frequency = generate_balance_frequency()
print(balance_frequency)  # Output: a random float between 0.5 and 2.0
