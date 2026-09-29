
def steps_recursive(steps):
    if steps <= 0:
        print("Done!")
        return

    print(f"steps: {steps}")
    steps_recursive(steps - 1)
    

steps_recursive(3)