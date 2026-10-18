import time

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

if __name__ == "__main__":
    print("Preparing 10,000,000 items...")
    data = list(range(10_000_000))
    target = 9_999_999  # Worst-case for linear search

    # Benchmark Linear Search
    t0 = time.perf_counter()
    idx_l = linear_search(data, target)
    time_l = time.perf_counter() - t0

    # Benchmark Binary Search
    t0 = time.perf_counter()
    idx_b = binary_search(data, target)
    time_b = time.perf_counter() - t0

    # Results
    print(f"\nLinear Search: Index {idx_l} in {time_l:.6f}s")
    print(f"Binary Search: Index {idx_b} in {time_b:.6f}s")
    print(f"\n🚀 Binary Search was roughly {time_l / time_b:,.0f}x faster!")