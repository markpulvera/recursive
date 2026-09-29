import time


def count_steps_iterative(steps):
    for i in range(steps, 0, -1):
        pass  # Simulated work per step


# Measure execution time
steps_count = 500

start_time = time.perf_counter()
count_steps_iterative(steps_count)
end_time = time.perf_counter()

elapsed_time = end_time - start_time
print(f"Iterative Time: {elapsed_time:.8f} seconds")


