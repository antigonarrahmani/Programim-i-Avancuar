#Function to calculate the nth Fibonacci number
# The Fibonacci sequence starts with 0 and 1
# Each subsequent number is the sum of the two preceding ones
# Example: 0, 1, 1, 2, 3, 5, 8, 13, ...
# Parameter: n (int) - the position in the sequence (0-indexed)
# Returns: the nth Fibonacci number

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
# Test the function with a few examples

print(fibonacci(0)) # Expected output: 0
print(fibonacci(1)) # Expected output: 1
print(fibonacci(2)) # Expected output: 1
print(fibonacci(3)) # Expected output: 2
print(fibonacci(4)) # Expected output: 3
print(fibonacci(5)) # Expected output: 5
print(fibonacci(6)) # Expected output: 8
print(fibonacci(7)) # Expected output: 13
print(fibonacci(8)) # Expected output: 21
print(fibonacci(9)) # Expected output: 34
print(fibonacci(10)) # Expected output: 55
print(fibonacci(11)) # Expected output: 89
print(fibonacci(12)) # Expected output: 144
print(fibonacci(13)) # Expected output: 233

#The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, usually starting with 0 and 1. In this Python program, we define a function fibonacci(n) that calculates the nth Fibonacci number using recursion. We test the function with a few examples to verify its correctness.

#Python Fibonacci Sequence Using Iteration