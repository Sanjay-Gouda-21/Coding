# Function to generate Fibonacci numbers
def fibonacci(n):
    fib_sequence = [0, 1]
    
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    
    return fib_sequence

# Get user input for the number of Fibonacci numbers to generate
num_terms = int(input("Enter the number of Fibonacci numbers to generate: "))

# Call the fibonacci function and print the result
result = fibonacci(num_terms)
print(f"The first {num_terms} Fibonacci numbers are: {result}")
