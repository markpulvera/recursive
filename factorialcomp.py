def factorial(n):
    # 1. BASE CASE: Stops recursion when n is 0 or 1
    if n <= 1:
        return 1
    
    # 2. RECURSIVE CASE: Function calls itself with (n - 1)
    return n * factorial(n - 1)


# Example execution
number = 10
result = factorial(number)
print(f"The factorial of {number} is {result}")