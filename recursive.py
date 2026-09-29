import time


def count_steps_recursive(steps):
    # Base Case
    if steps <= 0:
        return

    # Recursive Case
    count_steps_recursive(steps - 1)


# Measure execution time
steps_count = 500

start_time = time.perf_counter()
count_steps_recursive(steps_count)
end_time = time.perf_counter()

elapsed_time = end_time - start_time
print(f"Recursive Time: {elapsed_time:.8f} seconds")