#ITERATIVE
def total_step_combinations_iterative(steps_count: int) -> int:


    # base case
    if steps_count <= 1:
        return 1
    accumulated_steps_combination = 1

    # loop
    for current_step in range(steps_count, 1, -1):
        accumulated_steps_combination *= current_step
    return accumulated_steps_combination



#RECURSIVE
def total_step_combinations_recursive(steps_count: int) -> int:
    # base case
    if steps_count <= 1:
        return 1
    # recursive case
    return steps_count * total_step_combinations_recursive(steps_count - 1)


steps_count = 10


result_iterative = total_step_combinations_iterative(steps_count)
result_recursive = total_step_combinations_recursive(steps_count)


