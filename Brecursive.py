def binary_search_recursive(arr, target, left, right):
    # Base case: if pointers cross, element is not found
    if left > right:
        return -1
        
    mid = (left + right) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        # Search the right half
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        # Search the left half
        return binary_search_recursive(arr, target, left, mid - 1)

# Test Data (Must be sorted!)
sorted_numbers = [10, 15, 33, 42, 77, 91]
target_value = 15

result = binary_search_recursive(sorted_numbers, target_value, 0, len(sorted_numbers) - 1)
print(f"Binary Search (Recursive) Output: Element found at index {result}")