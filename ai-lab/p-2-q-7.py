# Experiment No: 07
# Experiment Name: Write a program to implement Hill Climbing Algorithm
# Source Code:

def hill_climbing(start):
    def objective(x):
        return -(x - 5) ** 2 + 25

    current = start
    while True:
        left = current - 1
        right = current + 1
        current_value = objective(current)
        left_value = objective(left)
        right_value = objective(right)

        if left_value > current_value:
            current = left
        elif right_value > current_value:
            current = right
        else:
            break

    return current, objective(current)


if __name__ == "__main__":
    start_point = 0
    best_x, best_value = hill_climbing(start_point)
    print("Best x =", best_x)
    print("Maximum value =", best_value)

# Output:
# Best x = 5
# Maximum value = 25