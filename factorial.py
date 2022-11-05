# Function to determine the factorial of a given number n

def factorial(n):
    output = 1
    for i in range(1, n + 1):
        output *= i
    return output