# Function to determine the factorial of a given number n

def factorial(n):
    output = 0
    for i in range(n):
        output *= i
    return output