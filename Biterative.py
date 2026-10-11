def binary_search_iterative(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1   # Discard left half
        else:
            right = mid - 1  # Discard right half
            
    return -1

# Test Data (Must be sorted!)
sorted_numbers = [10, 15, 33, 42, 77, 91]
target_value = 77

result = binary_search_iterative(sorted_numbers, target_value)
print(f"Binary Search (Iterative) Output: Element found at index {result}")