def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Returns the index of the target
    return -1         # Returns -1 if not found

# Test Data
numbers = [42, 10, 77, 33, 91, 15]
target_value = 33

result = linear_search(numbers, target_value)
print(f"Linear Search Output: Element found at index {result}")