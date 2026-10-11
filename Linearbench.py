import time

# Linear Search Function
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Setup Dataset
dataset = list(range(100000))
target_value = 99999  # Worst-case scenario (at the end)
runs = 1000

# Measure Linear Search Speed
start_time = time.time()
for _ in range(runs):
    linear_search(dataset, target_value)
linear_time = time.time() - start_time

# Display Results
print("--- Linear Search Benchmark ---")
print(f"Dataset Size: 100,000 items")
print(f"Time taken for {runs} runs: {linear_time:.6f} seconds")