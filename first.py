import time

def factorial(n):
    # 1. Base Case: stops the recursion
    if n <= 1:
        return 1

    # 2. Recursive Case: function calls itself with a smaller input
    return n * factorial(n - 1)


# Example usage
print(factorial(5)) 
