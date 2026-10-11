import time

# Binary Search Function
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Setup Dataset (Must be sorted for binary search)
dataset = list(range(100000))
target_value = 99999
runs = 1000

# Measure Binary Search Speed
start_time = time.time()
for _ in range(runs):
    binary_search(dataset, target_value)
binary_time = time.time() - start_time

# Display Results
print("--- Binary Search Benchmark ---")
print(f"Dataset Size: 100,000 items")
print(f"Time taken for {runs} runs: {binary_time:.6f} seconds")